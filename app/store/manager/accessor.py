from hashlib import sha256
from sqlalchemy import select, update
from sqlalchemy.orm import subqueryload, Session, joinedload
from sqlalchemy.orm.query import Query
from sqlalchemy.engine import ChunkedIteratorResult
from app.base.base_accessor import BaseAccessor
from app.manager.models import ManagerModel, ManagerAuthModel
from app.store.database.database import Database
from app.back.utils import is_valid_psw


class ManagerAccessor(BaseAccessor):
    def signup(self, email: str, password: str, auth_token: str):
        with self.app.database.session() as get_session:
            if not is_valid_psw(password):
                pass
            hashed_psw = sha256(password.encode()).hexdigest()
            subquery = select(ManagerModel.manager_id).where(
                ManagerModel.email_address == email
            )
            res: Query = get_session.query(ManagerAuthModel).filter(
                ManagerAuthModel.manager_id == subquery.scalar_subquery(),
                ManagerAuthModel.password_.is_(None),
                ManagerAuthModel.auth_token == auth_token
            ).update(
                {"password_": hashed_psw}, synchronize_session="fetch"
            )
            if res == 0:
                pass
            get_session.commit()
