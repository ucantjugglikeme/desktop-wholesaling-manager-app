from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App


class VendorGetView:
    def __init__(self, app: "App"):
        self.app = app

    def get(self) -> list[tuple[str, str, str, str, str]]:
        return self.app.store.vendors.list_vendors()
