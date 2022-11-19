from dataclasses import dataclass

from app.store.database.sqlalchemy_base import db
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    BigInteger,
    TEXT,
)


@dataclass
class Warehouse:
    warehouse_id: int
    warehouse_address: str


class WarehouseModel(db):
    __tablename__ = "Warehouse"
    warehouse_id = Column(BigInteger, primary_key=True)
    warehouse_address = Column(TEXT, nullable=False)
    product = relationship("ProductModel", backref="Warehouse")

    def __repr__(self):
        return f"<WarehouseModel(warehouse_id='{self.warehouse_id}', warehouse_address='{self.warehouse_address})>"
