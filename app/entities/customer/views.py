from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

from app.back.utils import define_info_dialog, set_up_info_dialog


class CustomerGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self, params: list[str | None]) -> list[tuple[str, str, str, str, str]]:
        query_params = {
            "customer_id": params[0],
            "customer_name": params[1],
            "customer_address": params[2],
            "email_address": params[3],
            "customer_number": params[4],
        }
        return self.app.store.customers.list_customers(**query_params)


class CustomerAddView:
    def __init__(self, app: "App"):
        self.app = app

    def add(self, params: list) -> tuple[str, str, str, str | None, str] | list[None]:
        query_params = {
            "customer_name": params[0],
            "customer_address": params[1],
            "customer_number": params[2],
            "email_address": params[3],
        }
        resp_data = self.app.store.customers.add_customer(**query_params)
        if not resp_data:
            set_up_info_dialog(
                self.app.m_win.info_dialog, self.app.m_win.info_form,
                "Нарушена целостность таблицы. Проверьте введенные данные",
                self.app.m_win.err_icon, self.app.m_win.err_img
            )
        return resp_data


class CustomerUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> tuple[str, str, str]:
        filter_params = {
            "customer_id": filter_vals[0],
            "customer_name": filter_vals[1],
            "customer_address": filter_vals[2],
            "email_address": filter_vals[3],
            "customer_number": filter_vals[4],
        }
        rows = self.app.store.customers.update_customers(upd_params, **filter_params)
        text = f'{rows} строк было изменено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]


class CustomerDeleteView:
    def __init__(self, app: "App"):
        self.app = app

    def delete(self, params: list[str | None]) -> tuple[str, str, str]:
        query_params = {
            "customer_id": params[0],
            "customer_name": params[1],
            "customer_address": params[2],
            "email_address": params[3],
            "customer_number": params[4],
        }
        rows = self.app.store.customers.delete_customers(**query_params)
        text = f'{rows} строк было удалено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]
