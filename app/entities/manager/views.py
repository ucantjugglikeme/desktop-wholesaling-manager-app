from typing import TYPE_CHECKING

from app.back.utils import define_info_dialog

if TYPE_CHECKING:
    from app import App
    from app.entities.manager.models import ManagerModel


class ManagerLogInView:
    def __init__(self, app: "App"):
        self.app = app

    def login(self, data: tuple[str, str] | list[str]) -> tuple[str, str, str, "ManagerModel"]:
        response_data = self.app.store.managers.login(
            data[0], data[1]
        )
        return response_data


class ManagerSignUpView:
    def __init__(self, app: "App"):
        self.app = app

    def signup(self, data: tuple[str, str, str] | list[str]) -> tuple[str, str, str]:
        response_data = self.app.store.managers.signup(
            data[0], data[1], data[2]
        )
        return response_data


class ManagerGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self, params: list[str | None]) -> list[tuple[str, str, str, str, str, str, str]]:
        query_params = {
            "manager_id": params[0],
            "manager_full_name": params[1],
            "birth_date": params[2],
            "department_number": params[3],
            "residential_address": params[4],
            "email_address": params[5],
            "work_number": params[6],
        }
        return self.app.store.managers.list_managers(**query_params)


class ManagerUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> tuple[str, str, str]:
        filter_params = {
            "manager_id": filter_vals[0],
            "manager_full_name": filter_vals[1],
            "birth_date": filter_vals[2],
            "department_number": filter_vals[3],
            "residential_address": filter_vals[4],
            "email_address": filter_vals[5],
            "work_number": filter_vals[6],
        }
        rows = self.app.store.managers.update_managers(upd_params, **filter_params)
        text = f'{rows} строк было изменено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]
