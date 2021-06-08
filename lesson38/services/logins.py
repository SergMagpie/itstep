from services.base import get_session, Session
from services.tables import User
from typing import List
import models


from fastapi import Depends


class Users:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get_all(self) -> List[User]:
        operations = (
            self.session
            .query(User.id, User.username)
            .order_by(
                User.username.desc(),
            )
            .all()
        )
        return operations

    def create(
        self,
        operation_data: models.UserCreate,
    ) -> User:
        operation = User(
            **operation_data.dict(),
        )
        self.session.add(operation)
        self.session.commit()
        return operation
