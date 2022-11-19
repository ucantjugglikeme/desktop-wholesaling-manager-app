from typing import List, Any, Tuple
from decimal import Decimal

from sqlalchemy import select, delete
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.engine.cursor import LegacyCursorResult
from sqlalchemy.exc import (
    IntegrityError, ProgrammingError,
    OperationalError, DataError
)
from app.base.base_accessor import BaseAccessor
from app.entities.product.models import ProductModel, ProductCategoryModel


class ProductAccessor(BaseAccessor):
    def list_products(
            self, **params: str | None
    ) -> list[tuple[str, str, str, str, str, str, str]]:
        filter_params = [
            comp_stmt for comp_stmt in [
                ProductModel.product_id == params["product_id"]
                if params["product_id"] is not None else None,
                ProductModel.product_name == params["product_name"]
                if params["product_name"] is not None else None,
                ProductModel.product_cost == params["product_cost"]
                if params["product_cost"] is not None else None,
                ProductModel.amount == params["amount"]
                if params["amount"] is not None else None,
                ProductModel.product_category_id == params["product_category_id"]
                if params["product_category_id"] is not None else None,
                ProductModel.warehouse_id == params["warehouse_id"]
                if params["warehouse_id"] is not None else None,
                ProductModel.vendor_id == params["vendor_id"]
                if params["vendor_id"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        # filter(lambda x: x is not None, filter_params) doesn't work :(
        select_query = select(ProductModel).where() if not filter_params \
            else select(ProductModel).where(*filter_params)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(
            str(row[0].product_id), row[0].product_name, str(row[0].product_cost),
            str(row[0].amount), str(row[0].product_category_id), str(row[0].warehouse_id),
            str(row[0].vendor_id)
        ) for row in raw_res_lst]

        return res_lst

    def list_categories(
            self, **params: str | None
    ) -> list[tuple[str, str]]:
        filter_params = [
            comp_stmt for comp_stmt in [
                ProductCategoryModel.product_category_id == params["product_category_id"]
                if params["product_category_id"] is not None else None,
                ProductCategoryModel.product_category == params["product_category"]
                if params["product_category"] is not None else None,
            ]
            if comp_stmt is not None
        ]
        # filter(lambda x: x is not None, filter_params) doesn't work :(
        select_query = select(ProductCategoryModel).where() if not filter_params \
            else select(ProductCategoryModel).where(*filter_params)

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        res_lst = [(str(row[0].product_category_id), row[0].product_category) for row in raw_res_lst]

        return res_lst

    def add_product(
            self, product_name: str, product_cost: Decimal, amount: int,
            product_category_id: int | None, warehouse_id: int, vendor_id: int | None
    ) -> list[Any] | tuple[str, str, str, str, str | None, str, str | None]:
        product = ProductModel(
            product_name=product_name, product_cost=product_cost, amount=amount,
            product_category_id=product_category_id, warehouse_id=warehouse_id, vendor_id=vendor_id
        )

        with self.app.database.session() as insert_session:
            insert_session.add(product)
            try:
                insert_session.commit()
            except IntegrityError:
                return []
            except ProgrammingError:
                return []

        res_lst = (
            str(product.product_id), product_name, str(product_cost), str(amount),
            str(product_category_id), str(warehouse_id), str(vendor_id)
        )
        return res_lst

    def add_category(self, product_category: str) -> list[Any] | tuple[str, str]:
        productcategory = ProductCategoryModel(product_category=product_category)

        with self.app.database.session() as insert_session:
            insert_session.add(productcategory)
            try:
                insert_session.commit()
            except IntegrityError:
                return []
            except ProgrammingError:
                return []

        res_lst = (str(productcategory.product_category_id), product_category)
        return res_lst

    def update_products(self, update_params: list[str], **filter_params: str | None) -> int | None:
        filter_values = [
            comp_stmt for comp_stmt in [
                ProductModel.product_id == filter_params["product_id"]
                if filter_params["product_id"] is not None else None,
                ProductModel.product_name == filter_params["product_name"]
                if filter_params["product_name"] is not None else None,
                ProductModel.product_cost == filter_params["product_cost"]
                if filter_params["product_cost"] is not None else None,
                ProductModel.amount == filter_params["amount"]
                if filter_params["amount"] is not None else None,
                ProductModel.product_category_id == filter_params["product_category_id"]
                if filter_params["product_category_id"] is not None else None,
                ProductModel.warehouse_id == filter_params["warehouse_id"]
                if filter_params["warehouse_id"] is not None else None,
                ProductModel.vendor_id == filter_params["vendor_id"]
                if filter_params["vendor_id"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        update_values = {
            val_name: value for val_name, value in {
                "product_name": update_params[0] if update_params[0] is not None else None,
                "product_cost": update_params[1] if update_params[1] is not None else None,
                "amount": update_params[2] if update_params[2] is not None else None,
                "product_category_id": update_params[3] if update_params[3] is not None else None,
                "warehouse_id": update_params[4] if update_params[4] is not None else None,
                "vendor_id": update_params[5] if update_params[5] is not None else None,
            }.items() if value is not None
        }

        with self.app.database.session() as update_session:
            try:
                res = update_session.query(ProductModel).filter(*filter_values).update(
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

    def update_categories(self, update_params: list[str], **filter_params: str | None) -> int | None:
        filter_values = [
            comp_stmt for comp_stmt in [
                ProductCategoryModel.product_category_id == filter_params["product_category_id"]
                if filter_params["product_category_id"] is not None else None,
                ProductCategoryModel.product_category == filter_params["product_category"]
                if filter_params["product_category"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        update_values = {
            val_name: value for val_name, value in {
                "product_category": update_params[0] if update_params[0] is not None else None,
            }.items() if value is not None
        }

        with self.app.database.session() as update_session:
            try:
                res = update_session.query(ProductCategoryModel).filter(*filter_values).update(
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

    def delete_products(self, **query_params: str | None) -> int | None:
        filter_params = [
            comp_stmt for comp_stmt in [
                ProductModel.product_id == query_params["product_id"]
                if query_params["product_id"] is not None else None,
                ProductModel.product_name == query_params["product_name"]
                if query_params["product_name"] is not None else None,
                ProductModel.product_cost == query_params["product_cost"]
                if query_params["product_cost"] is not None else None,
                ProductModel.amount == query_params["amount"]
                if query_params["amount"] is not None else None,
                ProductModel.product_category_id == query_params["product_category_id"]
                if query_params["product_category_id"] is not None else None,
                ProductModel.warehouse_id == query_params["warehouse_id"]
                if query_params["warehouse_id"] is not None else None,
                ProductModel.vendor_id == query_params["vendor_id"]
                if query_params["vendor_id"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        delete_query = delete(ProductModel).where(*filter_params)
        with self.app.database.session() as delete_session:
            try:
                res: LegacyCursorResult = delete_session.execute(delete_query)
            except OperationalError:
                return None
            rowcount = res.rowcount
            delete_session.commit()

        return rowcount

    def delete_categories(self, **query_params: str | None) -> int | None:
        filter_params = [
            comp_stmt for comp_stmt in [
                ProductModel.product_id == query_params["product_id"]
                if query_params["product_id"] is not None else None,
                ProductModel.product_name == query_params["product_name"]
                if query_params["product_name"] is not None else None,
                ProductModel.product_cost == query_params["product_cost"]
                if query_params["product_cost"] is not None else None,
                ProductModel.amount == query_params["amount"]
                if query_params["amount"] is not None else None,
                ProductModel.product_category_id == query_params["product_category_id"]
                if query_params["product_category_id"] is not None else None,
                ProductModel.warehouse_id == query_params["warehouse_id"]
                if query_params["warehouse_id"] is not None else None,
                ProductModel.vendor_id == query_params["vendor_id"]
                if query_params["vendor_id"] is not None else None,
            ]
            if comp_stmt is not None
        ]

        delete_query = delete(ProductModel).where(*filter_params)
        with self.app.database.session() as delete_session:
            try:
                res: LegacyCursorResult = delete_session.execute(delete_query)
            except OperationalError:
                return None
            rowcount = res.rowcount
            delete_session.commit()

        return rowcount
