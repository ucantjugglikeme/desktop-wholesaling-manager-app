from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App


class ManagerLoginView:
    def __init__(self, app: "App"):
        self.app = app

    def login(self):
        pass


class ManagerSignUpView:
    def __init__(self, app: "App"):
        self.app = app

    def signup(self, data: tuple | list):
        self.app.store.managers.signup(data[0], data[1], data[2])
