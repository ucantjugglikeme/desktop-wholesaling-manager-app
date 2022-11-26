from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.exc import ProgrammingError, DataError, IntegrityError

from app.base.base_accessor import BaseAccessor
from app.entities.manager.models import (
    ManagerModel, ManagerAuthModel
)
from app.back.utils import is_valid_psw, get_value_range, check_number_if_exists


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

    def list_managers(
            self, **params: str | None
    ) -> list[tuple[str, str, str, str, str, str, str]]:
        birth_date_range = get_value_range(params["birth_date"])
        department_range = get_value_range(params["department_number"])
        filter_params = [
            comp_stmt for comp_stmt in [
                ManagerModel.manager_id == params["manager_id"]
                if params["manager_id"] is not None else None,
                ManagerModel.manager_full_name.like(f"%{params['manager_full_name']}%")
                if params["manager_full_name"] is not None else None,
                ManagerModel.birth_date.between(birth_date_range[0], birth_date_range[1])
                if params["birth_date"] is not None else None,
                ManagerModel.department_number.between(department_range[0], department_range[1])
                if params["department_number"] is not None else None,
                ManagerModel.residential_address.like(f"%{params['residential_address']}%")
                if params["residential_address"] is not None else None,
                ManagerModel.email_address.like(f"%{params['email_address']}%")
                if params["email_address"] is not None else None,
                ManagerModel.work_number.like(f"%{params['work_number']}%")
                if params["work_number"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        # filter(lambda x: x is not None, filter_params) doesn't work :(
        select_query = select(ManagerModel) if not filter_params \
            else select(ManagerModel).filter(*filter_params)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(
            str(row[0].manager_id), row[0].manager_full_name, str(row[0].birth_date),
            str(row[0].department_number), row[0].residential_address, row[0].email_address,
            row[0].work_number,
        ) for row in raw_res_lst]

        return res_lst

    def update_managers(self, update_params: list[str], **filter_params: str | None) -> int | None:
        filter_values = [
            comp_stmt for comp_stmt in [
                ManagerModel.manager_id == filter_params["manager_id"]
                if filter_params["manager_id"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        update_values = {
            val_name: value for val_name, value in {
                "email_address": update_params[0] if update_params[0] is not None else None,
                "work_number": update_params[1] if update_params[1] is not None else None,
            }.items() if value is not None
        }

        try:
            resp = check_number_if_exists(update_values["work_number"], self.app)
        except KeyError:
            resp = None
        if resp is not None:
            return None

        with self.app.database.session() as update_session:
            try:
                res = update_session.query(ManagerModel).filter(*filter_values).update(
                    update_values, synchronize_session="fetch"
                )
            except ProgrammingError:
                res = 0
            except DataError:
                return None
            except IntegrityError:
                return None
            try:
                filter_values = [
                    comp_stmt for comp_stmt in [
                        ManagerAuthModel.manager_id == filter_params["manager_id"]
                        if filter_params["manager_id"] is not None else None,
                    ]
                    if comp_stmt is not None
                ]
                update_values = {
                    val_name: value for val_name, value in {
                        "password_": sha256(update_params[2].encode()).hexdigest() if update_params[2] is not None
                        else None,
                    }.items() if value is not None
                }
                res += update_session.query(ManagerAuthModel).filter(*filter_values).update(
                    update_values, synchronize_session="fetch"
                )
            except ProgrammingError:
                pass
            except DataError:
                return None
            except IntegrityError:
                return None
            update_session.commit()

        return res

    def get_p_keys(self) -> list[int]:
        select_query = select(ManagerModel.manager_id).order_by(ManagerModel.manager_id)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        return [p_key[0] for p_key in raw_res_lst]
