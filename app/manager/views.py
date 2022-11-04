from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App
    from app.manager.models import ManagerModel


class ManagerLogInView:
    def __init__(self, app: "App"):
        self.app = app

    def login(self, data: tuple[str, str] | list[str]) -> tuple[str, str, str, "ManagerModel"]:
        response_data = self.app.store.managers.login(
            data[0], data[1]
        )
        return response_data


class ManagerSignUpView:
    def __init__(self, app: "App"):
        self.app = app

    def signup(self, data: tuple[str, str, str] | list[str]) -> tuple[str, str, str]:
        response_data = self.app.store.managers.signup(
            data[0], data[1], data[2]
        )
        return response_data
