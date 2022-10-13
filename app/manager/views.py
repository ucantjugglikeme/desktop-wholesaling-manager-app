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

    def signup(self, data: tuple[str, str, str] | list[str]) -> tuple[str, str, str]:
        response_data = self.app.store.managers.signup(
            data[0], data[1], data[2]
        )
        return response_data
