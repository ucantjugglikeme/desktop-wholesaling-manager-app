from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

from app.back.utils import define_info_dialog, set_up_info_dialog


class VendorGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self, params: list[str | None]) -> list[tuple[str, str, str, str, str]]:
        query_params = {
            "vendor_id": params[0],
            "vendor_name": params[1],
            "vendor_address": params[2],
            "vendor_number": params[3],
            "email_address": params[4],
        }
        return self.app.store.vendors.list_vendors(**query_params)


class VendorAddView:
    def __init__(self, app: "App"):
        self.app = app

    def add(self, params: list[str | None]) -> tuple[str, str, str, str, str] | list[None]:
        query_params = {
            "vendor_name": params[0],
            "vendor_address": params[1],
            "vendor_number": params[2],
            "email_address": params[3],
        }
        resp_data = self.app.store.vendors.add_vendor(**query_params)
        if not resp_data:
            set_up_info_dialog(
                self.app.m_win.info_dialog, self.app.m_win.info_form,
                "Нарушена целостность таблицы. Проверьте введенные данные",
                self.app.m_win.err_icon, self.app.m_win.err_img
            )
        return resp_data


class VendorUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> tuple[str, str, str]:
        filter_params = {
            "vendor_id": filter_vals[0],
            "vendor_name": filter_vals[1],
            "vendor_address": filter_vals[2],
            "vendor_number": filter_vals[3],
            "email_address": filter_vals[4],
        }
        rows = self.app.store.vendors.update_vendors(upd_params, **filter_params)
        text = f'{rows} строк было изменено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]


class VendorDeleteView:
    def __init__(self, app: "App"):
        self.app = app

    def delete(self, params: list[str | None]) -> tuple[str, str, str]:
        query_params = {
            "vendor_id": params[0],
            "vendor_name": params[1],
            "vendor_address": params[2],
            "vendor_number": params[3],
            "email_address": params[4],
        }
        rows = self.app.store.vendors.delete_vendors(**query_params)
        text = f'{rows} строк было удалено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]
