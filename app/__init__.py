import sys
from PyQt5.QtWidgets import QApplication
from app.view.ui import Ui
from app.store import Store, setup_store
from app.back.config import DatabaseConfig, setup_config


class App:
    q_app: QApplication | None
    m_win: Ui | None
    config: DatabaseConfig | None
    store: Store | None
    database: object | None

    def __init__(self, q_app: QApplication):
        self.q_app = q_app

    def exec(self):
        self.m_win.show()
        return self.q_app.exec()


def setup_app(app_dir: str, config_path: str):
    q_app = QApplication([])
    app = App(q_app)
    m_window = Ui(app, app_dir)
    app.m_win = m_window

    setup_config(app, config_path)
    setup_store(app)

    sys.exit(app.exec())
