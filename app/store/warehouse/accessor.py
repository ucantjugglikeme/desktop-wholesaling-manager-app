from typing import List, Any, Tuple

from sqlalchemy import select, delete
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.cursor import LegacyCursorResult
from sqlalchemy.exc import (
    IntegrityError, ProgrammingError,
    OperationalError, DataError
)
from app.base.base_accessor import BaseAccessor
from app.entities.vendor.models import VendorModel
from app.entities.warehouse.models import WarehouseModel
from app.back.utils import check_number_if_exists, is_valid_number


class WarehouseAccessor(BaseAccessor):
    def list_warehouses(
            self, **params: str | None
    ) -> list[tuple[str, str]]:
        filter_params = [
            comp_stmt for comp_stmt in [
                WarehouseModel.warehouse_id == params["warehouse_id"]
                if params["warehouse_id"] is not None else None,
                WarehouseModel.warehouse_address == params["warehouse_address"]
                if params["warehouse_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        select_query = select(WarehouseModel).where() if not filter_params \
            else select(WarehouseModel).where(*filter_params)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(str(row[0].warehouse_id), row[0].warehouse_address) for row in raw_res_lst]
        return res_lst

    def add_warehouse(self, warehouse_address: str) -> list[None] | tuple[str, str]:
        warehouse = WarehouseModel(warehouse_address=warehouse_address)

        with self.app.database.session() as insert_session:
            insert_session.add(warehouse)
            try:
                insert_session.commit()
            except IntegrityError:
                return []
            except ProgrammingError:
                return []

        res_lst = (str(warehouse.warehouse_id), warehouse.warehouse_address)
        return res_lst

    def update_warehouse(self, update_params: list[str], **filter_params: str | None) -> int | None:
        filter_values = [
            comp_stmt for comp_stmt in [
                WarehouseModel.warehouse_id == filter_params["warehouse_id"]
                if filter_params["warehouse_id"] is not None else None,
                WarehouseModel.warehouse_address == filter_params["warehouse_address"]
                if filter_params["warehouse_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        update_values = {
            val_name: value for val_name, value in {
                "warehouse_address": update_params[0] if update_params[0] is not None else None,
            }.items() if value is not None
        }

        with self.app.database.session() as update_session:
            try:
                res = update_session.query(WarehouseModel).filter(*filter_values).update(
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

    def delete_warehouses(self, **query_params: str | None) -> int | None:
        filter_params = [
            comp_stmt for comp_stmt in [
                WarehouseModel.warehouse_id == query_params["warehouse_id"]
                if query_params["warehouse_id"] is not None else None,
                WarehouseModel.warehouse_address == query_params["warehouse_address"]
                if query_params["warehouse_address"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        delete_query = delete(WarehouseModel).where(*filter_params)
        with self.app.database.session() as delete_session:
            try:
                res: LegacyCursorResult = delete_session.execute(delete_query)
            except OperationalError:
                return None
            rowcount = res.rowcount
            delete_session.commit()

        return rowcount
