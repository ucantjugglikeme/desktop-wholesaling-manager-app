from typing import TYPE_CHECKING
from logging import getLogger

if TYPE_CHECKING:
    from app import App


class BaseAccessor:
    def __init__(self, app: "App"):
        self.app = app
        self.logger = getLogger("accessor")
