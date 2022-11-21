from dataclasses import dataclass

from app.store.database.sqlalchemy_base import db
from sqlalchemy import (
    Column,
    BigInteger,
    TEXT,
    VARCHAR,
)


@dataclass
class Customer:
    customer_id: int
    customer_name: str
    customer_address: str
    email_address: str
    customer_number: str


class CustomerModel(db):
    __tablename__ = "Customer"
    customer_id = Column(BigInteger, primary_key=True)
    customer_name = Column(TEXT, nullable=False)
    customer_address = Column(TEXT, nullable=False)
    email_address = Column(TEXT, nullable=True)
    customer_number = Column(VARCHAR(11), nullable=False)
    # managerauth = relationship("ManagerAuthModel", backref="manager", uselist=False)

    def __repr__(self):
        return f"<CustomerModel(" \
               f"customer_id='{self.customer_id}', customer_name='{self.customer_name}', " \
               f"customer_address='{self.customer_address}', email_address='{self.email_address}', " \
               f"customer_number='{self.customer_number}'" \
               f")>"
