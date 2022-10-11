from sqlalchemy import select
from sqlalchemy.orm import subqueryload, Session, joinedload
from sqlalchemy.engine import ChunkedIteratorResult
from app.base.base_accessor import BaseAccessor
from app.manager.models import ManagerModel, ManagerAuthModel
from app.store.database.database import Database


class ManagerAccessor(BaseAccessor):
    def login(self, email: str, password: str, auth_token: str):
        # query_get_manager = select(
            # ManagerModel.manager_id, ManagerModel.email_address,
            # ManagerAuthModel.password_, ManagerAuthModel.auth_token
        #    ManagerModel
        # ).where(ManagerModel.email_address == 'bicetufreigro-4581@yopmail.com').options(
        #     joinedload(ManagerModel.managerauth)
        # )

        query_get_manager = select(ManagerModel, ManagerAuthModel).where(
            ManagerModel.email_address == 'bicetufreigro-4581@yopmail.com'
        ).options(subqueryload(ManagerModel.managerauth))

        with self.app.database.session() as get_session:
            res: ChunkedIteratorResult = get_session.execute(query_get_manager)
            print(res.all())
            print(res.first())
            get_session.commit()
