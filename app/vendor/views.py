from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App


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

    def add(self, params: list[str | None]) -> list[tuple[str, str, str, str, str]] | list[tuple[None]]:
        query_params = {
            "vendor_name": params[0],
            "vendor_address": params[1],
            "vendor_number": params[2],
            "email_address": params[3],
        }
        return [self.app.store.vendors.add_vendor(**query_params)]


class VendorUpdateView:
    def __init__(self, app: "App"):
        self.app = app

    def update(self, filter_vals: list[str | None], upd_params: list[str | None]) -> \
            list[tuple[str, str, str, str, str]] | list[tuple[None]]:
        filter_params = {
            "vendor_id": filter_vals[0],
            "vendor_name": filter_vals[1],
            "vendor_address": filter_vals[2],
            "vendor_number": filter_vals[3],
            "email_address": filter_vals[4],
        }
        return self.app.store.vendors.update_vendors(upd_params, **filter_params)
