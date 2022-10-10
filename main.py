import os
from app import setup_app


if __name__ == "__main__":
    setup_app(os.path.dirname(os.path.realpath(__file__)))
