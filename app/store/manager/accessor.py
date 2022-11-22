from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from app.base.base_accessor import BaseAccessor
from app.entities.manager.models import (
    ManagerModel, ManagerAuthModel
)
from app.back.utils import is_valid_psw


class ManagerAccessor(BaseAccessor):
    def login(self, email: str, password: str) -> tuple[str, str, str, list]:
        with self.app.database.session() as get_session:
            hashed_psw = sha256(password.encode()).hexdigest()
            res: ChunkedIteratorResult = get_session.execute(select(
                ManagerModel, ManagerAuthModel.password_
            ).join(ManagerModel.managerauth).filter(
                ManagerModel.email_address == email,
                ManagerAuthModel.password_ == hashed_psw
            ))
            res_lst = res.all()
            if not res_lst:
                return (
                    "Проверьте введенные данные.\n\n"
                    "Пожалуйста, убедитесь в правильности введенных данных.\n"
                    "Проверьте адрес почты и пароль.\n"
                    "При затруднении свяжитесь с администратором.\n",
                    self.app.m_win.err_icon, self.app.m_win.err_img, []
                )
            get_session.commit()

        return (
            f"Здравствуйте, {res_lst[0][0].manager_full_name}!\n\nВы успешно авторизовались!",
            self.app.m_win.ok_icon, self.app.m_win.ok_img, res_lst[0][0]
        )

    def signup(self, email: str, password: str, auth_token: str) -> tuple[str, str, str]:
        with self.app.database.session() as upd_session:
            if not is_valid_psw(password):
                return (
                    "Слишком слабый пароль.\n\n"
                    "Пожалуйста, придумайте пароль длиной 8 и более символов.\n"
                    "Пароль должен содержать хотя бы 1 цифру, 1 маленькую латинскую\n"
                    "букву, 1 большую латинскую букву.",
                    self.app.m_win.warn_icon, self.app.m_win.warn_img,
                )
            hashed_psw = sha256(password.encode()).hexdigest()
            subquery = select(ManagerModel.manager_id).where(
                ManagerModel.email_address == email
            )
            res = upd_session.query(ManagerAuthModel).filter(
                ManagerAuthModel.manager_id == subquery.scalar_subquery(),
                ManagerAuthModel.password_.is_(None),
                ManagerAuthModel.auth_token == auth_token
            ).update(
                {"password_": hashed_psw}, synchronize_session="fetch"
            )
            if res == 0:
                return (
                    "Проверьте введенные данные.\n\n"
                    "Пожалуйста, убедитесь в правильности введенных данных.\n"
                    "Проверьте почту, регистрационный токен, пароль.\n"
                    "Возможно, аккаунт уже был зарегистрирован.\n"
                    "При затруднении свяжитесь с администратором.\n",
                    self.app.m_win.err_icon, self.app.m_win.err_img
                )
            upd_session.commit()

        return "Вы успешно зарегистрировались!", self.app.m_win.ok_icon, self.app.m_win.ok_img

    def get_p_keys(self) -> list[int]:
        select_query = select(ManagerModel.manager_id).order_by(ManagerModel.manager_id)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        return [p_key[0] for p_key in raw_res_lst]
