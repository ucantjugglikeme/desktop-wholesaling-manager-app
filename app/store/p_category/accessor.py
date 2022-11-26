from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult
from app.base.base_accessor import BaseAccessor
from app.entities.product.models import ProductCategoryModel


class ProductCategoryAccessor(BaseAccessor):
    def get_p_keys(self) -> list[int]:
        select_query = select(ProductCategoryModel.product_category_id).order_by(
            ProductCategoryModel.product_category_id
        )

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(select_query)
            raw_res_lst = res.all()
            get_session.commit()

        return [p_key[0] for p_key in raw_res_lst]
