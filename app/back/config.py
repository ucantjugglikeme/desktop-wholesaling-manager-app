import yaml
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from app import App


@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 3306
    user: str = "root"
    password: str = "123"
    dbname: str = "wholesaling"


def setup_config(app: "App", config_path: str):
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    app.config = DatabaseConfig(
        host=raw_config["database"]["host"],
        port=raw_config["database"]["port"],
        user=raw_config["database"]["user"],
        password=raw_config["database"]["password"],
        dbname=raw_config["database"]["dbname"],
    )
