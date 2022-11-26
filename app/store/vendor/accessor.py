from typing import List, Any, Tuple

from sqlalchemy import select, delete
from sqlalchemy.cimmutabledict import immutabledict
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.cursor import LegacyCursorResult
from sqlalchemy.exc import (
    IntegrityError, ProgrammingError,
    OperationalError, DataError
)
from app.base.base_accessor import BaseAccessor
from app.entities.vendor.models import VendorModel
from app.back.utils import check_number_if_exists, is_valid_number


class VendorAccessor(BaseAccessor):
    def list_vendors(
            self, **params: str | None
    ) -> list[tuple[str, str, str, str, str]]:
        filter_params = [
            comp_stmt for comp_stmt in [
                VendorModel.vendor_id == params["vendor_id"]
                if params["vendor_id"] is not None else None,
                VendorModel.vendor_name.like(f"%{params['vendor_name']}%")
                if params["vendor_name"] is not None else None,
                VendorModel.vendor_address.like(f"%{params['vendor_address']}%")
                if params["vendor_address"] is not None else None,
                VendorModel.vendor_number.like(f"%{params['vendor_number']}%")
                if params["vendor_number"] is not None else None,
                VendorModel.email_address.like(f"%{params['email_address']}%")
                if params["email_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        # filter(lambda x: x is not None, filter_params) doesn't work :(
        select_query = select(VendorModel) if not filter_params \
            else select(VendorModel).filter(*filter_params)

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
        if vendor_number is not None and not is_valid_number(vendor_number):
            return []

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
            except ProgrammingError:
                return []

        res_lst = (str(vendor.vendor_id), vendor_name, vendor_address, vendor_number, email_address)
        return res_lst

    def update_vendors(self, update_params: list[str], **filter_params: str | None) -> int | None:
        filter_values = [
            comp_stmt for comp_stmt in [
                VendorModel.vendor_id == filter_params["vendor_id"]
                if filter_params["vendor_id"] is not None else None,
                VendorModel.vendor_name.like(f"%{filter_params['vendor_name']}%")
                if filter_params["vendor_name"] is not None else None,
                VendorModel.vendor_address.like(f"%{filter_params['vendor_address']}%")
                if filter_params["vendor_address"] is not None else None,
                VendorModel.vendor_number.like(f"%{filter_params['vendor_number']}%")
                if filter_params["vendor_number"] is not None else None,
                VendorModel.email_address.like(f"%{filter_params['email_address']}%")
                if filter_params["email_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        update_values = {
            val_name: value for val_name, value in {
                "vendor_name": update_params[0] if update_params[0] is not None else None,
                "vendor_address": update_params[1] if update_params[1] is not None else None,
                "vendor_number": update_params[2] if update_params[2] is not None else None,
                "email_address": update_params[3] if update_params[3] is not None else None,
            }.items() if value is not None
        }

        try:
            resp = check_number_if_exists(update_values["vendor_number"], self.app)
        except KeyError:
            resp = None
        if resp is not None:
            return None

        with self.app.database.session() as update_session:
            try:
                res = update_session.query(VendorModel).filter(*filter_values).update(
                    update_values, synchronize_session="fetch"
                )
            except ProgrammingError:
                return None
            except DataError:
                return None
            except IntegrityError:
                return None
            update_session.commit()

        return res

    def delete_vendors(self, **query_params: str | None) -> int | None:
        filter_params = [
            comp_stmt for comp_stmt in [
                VendorModel.vendor_id == query_params["vendor_id"]
                if query_params["vendor_id"] is not None else None,
                VendorModel.vendor_name.like(f"%{query_params['vendor_name']}%")
                if query_params["vendor_name"] is not None else None,
                VendorModel.vendor_address.like(f"%{query_params['vendor_address']}%")
                if query_params["vendor_address"] is not None else None,
                VendorModel.vendor_number.like(f"%{query_params['vendor_number']}%")
                if query_params["vendor_number"] is not None else None,
                VendorModel.email_address.like(f"%{query_params['email_address']}%")
                if query_params["email_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        delete_query = delete(VendorModel).where(*filter_params)
        with self.app.database.session() as delete_session:
            try:
                res: LegacyCursorResult = delete_session.execute(
                    delete_query, execution_options=immutabledict({"synchronize_session": 'fetch'})
                )
            except OperationalError:
                return None
            rowcount = res.rowcount
            delete_session.commit()

        return rowcount

    def get_p_keys(self) -> list[int]:
        select_query = select(VendorModel.vendor_id).order_by(VendorModel.vendor_id)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        return [p_key[0] for p_key in raw_res_lst]

