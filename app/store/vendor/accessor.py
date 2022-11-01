from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.row import Row
from app.base.base_accessor import BaseAccessor
from app.vendor.models import VendorModel


class VendorAccessor(BaseAccessor):
    def list_vendors(
            self, vendor_id: int | None = None,
            vendor_address: str | None = None,
            vendor_number: str | None = None,
            email_address: str | None = None
    ) -> list[tuple[str, str, str, str, str]]:
        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select(VendorModel))
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(
            str(row[0].vendor_id), row[0].vendor_name, row[0].vendor_address,
            row[0].vendor_number, row[0].email_address
        ) for row in raw_res_lst]

        return res_lst
