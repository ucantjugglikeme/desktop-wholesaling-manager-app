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
