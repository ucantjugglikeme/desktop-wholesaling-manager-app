from hashlib import sha256
from sqlalchemy import select
from app.base.base_accessor import BaseAccessor
from app.manager.models import ManagerModel, ManagerAuthModel
from app.back.utils import is_valid_psw


class ManagerAccessor(BaseAccessor):
    def signup(self, email: str, password: str, auth_token: str) -> tuple[str, str, str]:
        with self.app.database.session() as get_session:
            if not is_valid_psw(password):
                return (
                    f"{self.app.m_win.app_dir}/resources/warning-icon.png",
                    f"{self.app.m_win.app_dir}/resources/warning.png",
                    "Слишком слабый пароль.\n\n"
                    "Пожалуйста, придумайте пароль длиной 8 и более символов.\n"
                    "Пароль должен содержать хотя бы 1 цифру, 1 маленькую латинскую\n"
                    "букву, 1 большую латинскую букву."
                )
            hashed_psw = sha256(password.encode()).hexdigest()
            subquery = select(ManagerModel.manager_id).where(
                ManagerModel.email_address == email
            )
            res = get_session.query(ManagerAuthModel).filter(
                ManagerAuthModel.manager_id == subquery.scalar_subquery(),
                ManagerAuthModel.password_.is_(None),
                ManagerAuthModel.auth_token == auth_token
            ).update(
                {"password_": hashed_psw}, synchronize_session="fetch"
            )
            if res == 0:
                return (
                    f"{self.app.m_win.app_dir}/resources/error-icon.png",
                    f"{self.app.m_win.app_dir}/resources/error.png",
                    "Проверьте введенные данные.\n\n"
                    "Пожалуйста, убедитесь в правильности введенных данных.\n"
                    "Проверьте почту, регистрационный токен, пароль.\n"
                    "Возможно, аккаунт уже был зарегистрирован.\n"
                    "При затруднении свяжитесь с администратором.\n"
                )
            get_session.commit()
        return (
            f"{self.app.m_win.app_dir}/resources/ok-mark-icon.png",
            f"{self.app.m_win.app_dir}/resources/ok-mark-v2.png",
            "Вы успешно зарегистрировались!"
        )
