from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

from app.back.utils import define_info_dialog, set_up_info_dialog


class ProductGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self, params: list[str | None]) -> list[tuple[str, str, str, str, str, str, str]]:
        query_params = {
            "product_id": params[0],
            "product_name": params[4],
            "product_cost": params[5],
            "amount": params[6],
            "product_category_id": params[1],
            "warehouse_id": params[2],
            "vendor_id": params[3],
        }
        return self.app.store.products.list_products(**query_params)


class ProductCategoryGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self, params: list[str | None]) -> list[tuple[str, str]]:
        query_params = {
            "product_category_id": params[0],
            "product_category": params[1],
        }
        return self.app.store.products.list_categories(**query_params)


class ProductAddView:
    def __init__(self, app: "App"):
        self.app = app

    def add(self, params: list) -> tuple[str, str, str, str, str] | list[None]:
        query_params = {
            "product_name": params[0],
            "product_cost": params[1],
            "amount": params[2],
            "product_category_id": params[3],
            "warehouse_id": params[4],
            "vendor_id": params[5],
        }
        resp_data = self.app.store.products.add_product(**query_params)
        if not resp_data:
            set_up_info_dialog(
                self.app.m_win.info_dialog, self.app.m_win.info_form,
                "Нарушена целостность таблицы. Проверьте введенные данные",
                self.app.m_win.err_icon, self.app.m_win.err_img
            )
        return resp_data


class ProductCategoryAddView:
    def __init__(self, app: "App"):
        self.app = app

    def add(self, params: list) -> tuple[str, str] | list[None]:
        query_params = {"product_category": params[0], }
        resp_data = self.app.store.products.add_category(**query_params)
        if not resp_data:
            set_up_info_dialog(
                self.app.m_win.info_dialog, self.app.m_win.info_form,
                "Нарушена целостность таблицы. Проверьте введенные данные",
                self.app.m_win.err_icon, self.app.m_win.err_img
            )
        return resp_data


class ProductUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> tuple[str, str, str]:
        filter_params = {
            "product_id": filter_vals[0],
            "product_name": filter_vals[1],
            "product_cost": filter_vals[2],
            "amount": filter_vals[3],
            "product_category_id": filter_vals[4],
            "warehouse_id": filter_vals[5],
            "vendor_id": filter_vals[6],
        }
        rows = self.app.store.products.update_products(upd_params, **filter_params)
        text = f'{rows} строк было изменено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]


class ProductCategoryUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> tuple[str, str, str]:
        filter_params = {
            "product_category_id": filter_vals[0],
            "product_category": filter_vals[1],
        }
        rows = self.app.store.products.update_categories(upd_params, **filter_params)
        text = f'{rows} строк было изменено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]


class ProductDeleteView:
    def __init__(self, app: "App"):
        self.app = app

    def delete(self, params: list[str | None]) -> tuple[str, str, str]:
        query_params = {
            "product_id": params[0],
            "product_name": params[4],
            "product_cost": params[5],
            "amount": params[6],
            "product_category_id": params[1],
            "warehouse_id": params[2],
            "vendor_id": params[3],
        }
        rows = self.app.store.products.delete_products(**query_params)
        text = f'{rows} строк было удалено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]


class ProductCategoryDeleteView:
    def __init__(self, app: "App"):
        self.app = app

    def delete(self, params: list[str | None]) -> tuple[str, str, str]:
        query_params = {
            "product_category_id": params[0],
            "product_category": params[1],
        }
        rows = self.app.store.products.delete_categories(**query_params)
        text = f'{rows} строк было удалено!' if rows is not None else 'Введены некорректные данные!'
        info = define_info_dialog(rows, self.app.m_win)
        return text, info[0], info[1]
