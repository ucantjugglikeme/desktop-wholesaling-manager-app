from typing import TYPE_CHECKING
from app.store.database.database import Database

if TYPE_CHECKING:
    from app import App


class Store:
    def __init__(self, app: "App"):
        # TODO: import accessors
        # self.accessor = Accessor(app)
        pass


def setup_store(app: "App"):
    # TODO: add database
    app.database = Database(app)
    app.database.connect()
    app.store = Store(app)
