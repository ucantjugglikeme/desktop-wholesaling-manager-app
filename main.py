import os
from app import setup_app


if __name__ == "__main__":
    setup_app(
        os.path.dirname(os.path.realpath(__file__)),
        os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "db_config.yml"
        )
    )
