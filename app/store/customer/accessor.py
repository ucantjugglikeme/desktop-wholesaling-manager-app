from typing import List, Any, Tuple

from sqlalchemy import select, delete
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.cursor import LegacyCursorResult
from sqlalchemy.exc import (
    IntegrityError, ProgrammingError,
    OperationalError, DataError
)
from app.base.base_accessor import BaseAccessor
from app.entities.customer.models import CustomerModel
from app.back.utils import check_number_if_exists, is_valid_number


class CustomerAccessor(BaseAccessor):
    def list_customers(
            self, **params: str | None
    ) -> list[tuple[str, str, str, str, str]]:
        filter_params = [
            comp_stmt for comp_stmt in [
                CustomerModel.customer_id == params["customer_id"]
                if params["customer_id"] is not None else None,
                CustomerModel.customer_name == params["customer_name"]
                if params["customer_name"] is not None else None,
                CustomerModel.customer_address == params["customer_address"]
                if params["customer_address"] is not None else None,
                CustomerModel.email_address == params["email_address"]
                if params["email_address"] is not None else None,
                CustomerModel.customer_number == params["customer_number"]
                if params["customer_number"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        # filter(lambda x: x is not None, filter_params) doesn't work :(
        select_query = select(CustomerModel).where() if not filter_params \
            else select(CustomerModel).where(*filter_params)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(
            str(row[0].customer_id), row[0].customer_name, row[0].customer_address,
            row[0].email_address, row[0].customer_number
        ) for row in raw_res_lst]

        return res_lst

    def add_customer(
            self, customer_name: str, customer_address: str, email_address: str | None, customer_number: str
    ) -> list[None] | tuple[str, str, str, str | None, str]:
        customer = CustomerModel(
            customer_name=customer_name, customer_address=customer_address,
            email_address=email_address, customer_number=customer_number
        )

        with self.app.database.session() as insert_session:
            insert_session.add(customer)
            try:
                insert_session.commit()
            except IntegrityError:
                return []
            except ProgrammingError:
                return []

        res_lst = (str(customer.customer_id), customer_name, customer_address, email_address, customer_number)
        return res_lst

    def update_customers(self, update_params: list[str], **filter_params: str | None) -> int | None:
        filter_values = [
            comp_stmt for comp_stmt in [
                CustomerModel.customer_id == filter_params["customer_id"]
                if filter_params["customer_id"] is not None else None,
                CustomerModel.customer_name == filter_params["customer_name"]
                if filter_params["customer_name"] is not None else None,
                CustomerModel.customer_address == filter_params["customer_address"]
                if filter_params["customer_address"] is not None else None,
                CustomerModel.email_address == filter_params["email_address"]
                if filter_params["email_address"] is not None else None,
                CustomerModel.customer_number == filter_params["customer_number"]
                if filter_params["customer_number"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        update_values = {
            val_name: value for val_name, value in {
                "customer_name": update_params[0] if update_params[0] is not None else None,
                "customer_address": update_params[1] if update_params[1] is not None else None,
                "email_address": update_params[2] if update_params[2] is not None else None,
                "customer_number": update_params[3] if update_params[3] is not None else None,
            }.items() if value is not None
        }

        with self.app.database.session() as update_session:
            try:
                res = update_session.query(CustomerModel).filter(*filter_values).update(
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

    def delete_customers(self, **query_params: str | None) -> int | None:
        filter_params = [
            comp_stmt for comp_stmt in [
                CustomerModel.customer_id == query_params["customer_id"]
                if query_params["customer_id"] is not None else None,
                CustomerModel.customer_name == query_params["customer_name"]
                if query_params["customer_name"] is not None else None,
                CustomerModel.customer_address == query_params["customer_address"]
                if query_params["customer_address"] is not None else None,
                CustomerModel.email_address == query_params["email_address"]
                if query_params["email_address"] is not None else None,
                CustomerModel.customer_number == query_params["customer_number"]
                if query_params["customer_number"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        delete_query = delete(CustomerModel).where(*filter_params)
        with self.app.database.session() as delete_session:
            try:
                res: LegacyCursorResult = delete_session.execute(delete_query)
            except OperationalError:
                return None
            rowcount = res.rowcount
            delete_session.commit()

        return rowcount

    def get_p_keys(self) -> list[int]:
        select_query = select(CustomerModel.customer_id).order_by(CustomerModel.customer_id)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        return [p_key[0] for p_key in raw_res_lst]
