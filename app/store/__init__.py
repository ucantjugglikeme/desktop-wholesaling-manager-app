from typing import TYPE_CHECKING
from app.store.database.database import Database
from app.store.manager.accessor import ManagerAccessor
from app.store.vendor.accessor import VendorAccessor
from app.store.warehouse.accessor import WarehouseAccessor
from app.store.product.accessor import ProductAccessor

if TYPE_CHECKING:
    from app import App


class Store:
    def __init__(self, app: "App"):
        # TODO: import accessors
        # self.accessor = Accessor(app)
        self.managers = ManagerAccessor(app)
        self.vendors = VendorAccessor(app)
        self.warehouses = WarehouseAccessor(app)
        self.products = ProductAccessor(app)


def setup_store(app: "App"):
    app.database = Database(app)
    app.database.connect()
    app.store = Store(app)
