from dataclasses import dataclass

from app.store.database.sqlalchemy_base import db
from sqlalchemy import (
    Column,
    BigInteger,
    TEXT,
)


@dataclass
class Vendor:
    vendor_id: int
    vendor_name: str
    vendor_address: str
    vendor_number: str
    email_address: str | None


class VendorModel(db):
    __tablename__ = "Vendor"
    vendor_id = Column(BigInteger, primary_key=True)
    vendor_name = Column(TEXT, nullable=False)
    vendor_address = Column(TEXT, nullable=False)
    vendor_number = Column(TEXT, nullable=False)
    email_address = Column(TEXT, nullable=True)

    def __repr__(self):
        return f"<VendorModel(" \
               f"vendor_id='{self.vendor_id}', vendor_name='{self.vendor_name}', " \
               f"vendor_address='{self.vendor_address}', vendor_number='{self.vendor_number}', " \
               f"email_address='{self.email_address}')>"
