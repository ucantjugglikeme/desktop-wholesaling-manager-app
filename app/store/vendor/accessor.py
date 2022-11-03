from hashlib import sha256
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.row import Row
from app.base.base_accessor import BaseAccessor
from app.vendor.models import VendorModel


class VendorAccessor(BaseAccessor):
    def list_vendors(
            self, **params: str | None
    ) -> list[tuple[str, str, str, str, str]]:
        filter_params = [
            comp_stmt for comp_stmt in [
                VendorModel.vendor_id == params["vendor_id"]
                if params["vendor_id"] is not None else None,
                VendorModel.vendor_name == params["vendor_name"]
                if params["vendor_name"] is not None else None,
                VendorModel.vendor_address == params["vendor_address"]
                if params["vendor_address"] is not None else None,
                VendorModel.vendor_number == params["vendor_number"]
                if params["vendor_number"] is not None else None,
                VendorModel.email_address == params["email_address"]
                if params["email_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        # filter(lambda x: x is not None, filter_params) doesn't work :(
        select_query = select(VendorModel).where() if not filter_params \
            else select(VendorModel).where(*filter_params)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(
            str(row[0].vendor_id), row[0].vendor_name, row[0].vendor_address,
            row[0].vendor_number, row[0].email_address
        ) for row in raw_res_lst]

        return res_lst
