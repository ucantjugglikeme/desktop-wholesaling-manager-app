from typing import TYPE_CHECKING
from logging import getLogger
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from app.store.database.sqlalchemy_base import db

if TYPE_CHECKING:
    from app import App


class BaseAccessor:
    def __init__(self, app: "App"):
        self.app = app
        self.logger = getLogger("accessor")

    def get_p_keys(self):
        pass
