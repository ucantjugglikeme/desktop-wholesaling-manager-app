from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

from app.back.utils import define_info_dialog, set_up_info_dialog


class WarehouseGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self, params: list[str | None]) -> list[tuple[str, str]]:
        query_params = {
            "warehouse_id": params[0],
            "warehouse_address": params[1],
        }
        return self.app.store.warehouses.list_warehouses(**query_params)


class WarehouseAddView:
    def __init__(self, app: "App"):
        self.app = app

    def add(self, params: list[str | None]) -> list[tuple[str, str]]:
        query_params = {"warehouse_address": params[0], }
        resp_data = self.app.store.warehouses.add_warehouse(**query_params)
        if not resp_data:
            set_up_info_dialog(
                self.app.m_win.info_dialog, self.app.m_win.info_form,
                "Нарушена целостность таблицы. Проверьте введенные данные",
                self.app.m_win.err_icon, self.app.m_win.err_img
            )
        return resp_data


class WarehouseUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> tuple[str, str, str]:
        filter_params = {
            "warehouse_id": filter_vals[0],
            "warehouse_address": filter_vals[1],
        }
        rows = self.app.store.warehouses.update_warehouse(upd_params, **filter_params)
        text = f'{rows} строк было изменено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]
