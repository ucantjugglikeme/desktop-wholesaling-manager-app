from typing import Optional, TYPE_CHECKING
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import Engine
from app.store.database.sqlalchemy_base import db

if TYPE_CHECKING:
    from app import App


class Database:
    def __init__(self, app: "App"):
        self.app = app
        self._db: Optional[declarative_base] = None
        self._engine: Engine | None
        self.session: Optional[sessionmaker] = None

    def connect(self) -> None:
        self._db = db

        db_config = self.app.config
        self._engine = create_engine(
            f"mysql+pymysql://{db_config.user}:{db_config.password}"
            f"@{db_config.host}:{db_config.port}/{db_config.dbname}"
        )

        self.session = sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
            class_=Engine
        )

    def disconnect(self) -> None:
        self.session.close_all()
