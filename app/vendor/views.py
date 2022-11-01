from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App


class VendorGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self) -> tuple[str, str, str, str, str]:
        response_data = self.app.store.vendors.list_vendors()
        table_data = response_data
        table_data[0] = str(table_data[0])
        return table_data
