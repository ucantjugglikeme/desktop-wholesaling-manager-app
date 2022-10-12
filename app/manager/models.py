from dataclasses import dataclass
from hashlib import sha256
from datetime import date

from app.store.database.sqlalchemy_base import db
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    BigInteger,
    TEXT,
    DATE,
    VARCHAR,
    ForeignKey,
)


@dataclass
class Manager:
    manager_id: int
    manager_full_name: str
    birth_date: date
    department_number: int
    residential_address: str
    email_address: str
    work_number: str


@dataclass
class ManagerAuth:
    manager_id: int
    password: str | None
    auth_token: str

    def is_password_valid(self, password: str) -> bool:
        return self.password == sha256(password.encode()).hexdigest()


class ManagerModel(db):
    __tablename__ = "Manager"
    manager_id = Column(BigInteger, primary_key=True)
    manager_full_name = Column(TEXT, nullable=False)
    birth_date = Column(DATE, nullable=False)
    department_number = Column(BigInteger, nullable=False)
    residential_address = Column(TEXT, nullable=False)
    email_address = Column(TEXT, nullable=False)
    work_number = Column(VARCHAR(11), nullable=False)
    managerauth = relationship("ManagerAuthModel", backref="manager", uselist=False)

    def __repr__(self):
        return f"<ManagerModel(" \
               f"manager_id='{self.manager_id}', manager_full_name='{self.manager_full_name}', " \
               f"birth_date='{self.birth_date}', department_number='{self.department_number}', " \
               f"residential_address='{self.residential_address}', email_address='{self.email_address}', " \
               f"work_number='{self.work_number}'" \
               f")>"


class ManagerAuthModel(db):
    __tablename__ = "ManagerAuth"
    manager_id = Column(BigInteger, ForeignKey("Manager.manager_id"), primary_key=True, autoincrement=False)
    password_ = Column(TEXT, nullable=True)
    auth_token = Column(TEXT, nullable=False)

    def __repr__(self):
        return f"<ManagerAuthModel(" \
               f"manager_id='{self.manager_id}', password_='{self.password_}', " \
               f"auth_token='{self.auth_token}'" \
               f")>"
