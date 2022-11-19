from dataclasses import dataclass
from decimal import Decimal

from app.store.database.sqlalchemy_base import db
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    BigInteger,
    INT,
    TEXT,
    ForeignKey,
    DECIMAL
)


@dataclass
class Product:
    product_id: int
    product_name: str
    product_cost: Decimal
    amount: int
    product_category_id: int | None
    warehouse_id: int
    vendor_id: int | None


@dataclass
class ProductCategory:
    product_category_id: int
    product_category: str


class ProductModel(db):
    __tablename__ = "Product"
    product_id = Column(BigInteger, primary_key=True)
    product_name = Column(TEXT, nullable=False)
    product_cost = Column(DECIMAL, nullable=False)
    amount = Column(INT, nullable=False)
    product_category_id = Column(BigInteger, ForeignKey("ProductCategory.product_category_id"), nullable=True)
    warehouse_id = Column(BigInteger, ForeignKey("Warehouse.warehouse_id"), nullable=False)
    vendor_id = Column(BigInteger, ForeignKey("Vendor.vendor_id"), nullable=True)

    def __repr__(self):
        return f"<ProductModel(" \
               f"product_id='{self.product_id}', product_name='{self.product_name}', " \
               f"product_cost='{self.product_cost}', amount='{self.amount}', " \
               f"product_category_id='{self.product_category_id}', warehouse_id='{self.warehouse_id}', " \
               f"vendor_id='{self.vendor_id}'" \
               f")>"


class ProductCategoryModel(db):
    __tablename__ = "ProductCategory"
    product_category_id = Column(BigInteger, primary_key=True)
    product_category = Column(TEXT, nullable=False)
    product = relationship("ProductModel", backref="ProductCategory")

    def __repr__(self):
        return f"<ProductCategoryModel(" \
               f"product_category_id='{self.product_category_id}', product_category='{self.product_category}'" \
               f")>"
