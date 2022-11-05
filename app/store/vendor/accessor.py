from hashlib import sha256
from typing import List, Any, Tuple

from sqlalchemy import select, insert
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.row import Row
from sqlalchemy.exc import IntegrityError
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

    def add_vendor(self, vendor_name: str, vendor_address: str, vendor_number: str, email_address: str | None) -> \
            list[None] | tuple[str, str, str, str, str | None]:
        vendor = VendorModel(
            vendor_name=vendor_name, vendor_address=vendor_address,
            vendor_number=vendor_number, email_address=email_address
        )

        with self.app.database.session() as insert_session:
            insert_session.add(vendor)
            try:
                insert_session.commit()
            except IntegrityError:
                return []

        res_lst = (str(vendor.vendor_id), vendor_name, vendor_address, vendor_number, email_address)
        return res_lst

    def update_vendors(
            self, update_params: list[str], **filter_params: str | None
    ) -> list[tuple[str, str, str, str, str]]:
        # TODO: define what should this method return

        print(filter_params)

        filter_values = [
            comp_stmt for comp_stmt in [
                VendorModel.vendor_id == filter_params["vendor_id"]
                if filter_params["vendor_id"] is not None else None,
                VendorModel.vendor_name == filter_params["vendor_name"]
                if filter_params["vendor_name"] is not None else None,
                VendorModel.vendor_address == filter_params["vendor_address"]
                if filter_params["vendor_address"] is not None else None,
                VendorModel.vendor_number == filter_params["vendor_number"]
                if filter_params["vendor_number"] is not None else None,
                VendorModel.email_address == filter_params["email_address"]
                if filter_params["email_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        print(filter_values)

        update_values = {
            val_name: value for val_name, value in {
                "vendor_name": update_params[0] if update_params[0] is not None else None,
                "vendor_address": update_params[1] if update_params[1] is not None else None,
                "vendor_number": update_params[2] if update_params[2] is not None else None,
                "email_address": update_params[3] if update_params[3] is not None else None,
            }.items() if value is not None
        }

        print(update_values)

        with self.app.database.session() as update_session:
            res = update_session.query(VendorModel).filter(*filter_values).update(
                update_values, synchronize_session="fetch"
            )
            if res == 0:
                print("update failed")
            else:
                print("update is ok")
            update_session.commit()

        return [("", "", "", "", "")]