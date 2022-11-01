from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from app.base.base_accessor import BaseAccessor
from app.vendor.models import VendorModel


class VendorAccessor(BaseAccessor):
    def list_vendors(
            self, vendor_id: int | None = None,
            vendor_address: str | None = None,
            vendor_number: str | None = None,
            email_address: str | None = None
    ) -> list[int, str, str, str, str]:
        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select(VendorModel))
            res_lst = res.all()
            get_session.commit()
        return res_lst
