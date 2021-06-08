from services.logins import Users
from services.base import get_session, Session
from services.tables import Operation, User
from typing import List, Optional
import models
from datetime import date

from fastapi import Depends, status, HTTPException


class Operations:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get_all(self, begin, end) -> List[Operation]:
        if end is None and isinstance(begin, date):
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.date >= begin)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        elif isinstance(end, date) and isinstance(begin, date):
            if begin > end:
                begin, end = end, begin
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.date >= begin,
                        Operation.date <= end)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        else:
            operations = (
                self.session
                .query(Operation)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        return operations

    def get_incomes(self, begin, end) -> List[Operation]:
        if end is None and isinstance(begin, date):
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.date >= begin,
                        Operation.money_amount > 0)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        elif isinstance(end, date) and isinstance(begin, date):
            if begin > end:
                begin, end = end, begin
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.date >= begin,
                        Operation.date <= end,
                        Operation.money_amount > 0)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        else:
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.money_amount > 0)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        return operations

    def get_outcomes(self, begin, end) -> List[Operation]:
        if end is None and isinstance(begin, date):
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.date >= begin,
                        Operation.money_amount < 0)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        elif isinstance(end, date) and isinstance(begin, date):
            if begin > end:
                begin, end = end, begin
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.date >= begin,
                        Operation.date <= end,
                        Operation.money_amount < 0)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        else:
            operations = (
                self.session
                .query(Operation)
                .filter(Operation.money_amount < 0)
                .order_by(
                    Operation.date.desc(),
                    Operation.id.desc(),
                )
                .all()
            )
        return operations

    def create(
        self,
        operation_data: models.OperationCreate,
    ) -> Operation:
        operation = Operation(
            **operation_data.dict(),
        )
        self.session.add(operation)
        self.session.commit()
        return operation

    def delete(
        self,
        operation_id: int,
    ):
        operation = self._get(operation_id)
        self.session.delete(operation)
        self.session.commit()

    def update(
        self,
        operation_id: int,
        operation_data: models.Operation,
    ) -> Operation:
        operation = self._get(operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def get_id(self,
               operation_id: int,
               username: str,
               password: str) -> Operation:
        user_id = (self.session
                   .query(User.id)
                   .filter(User.username == username,
                           User.password == password,
                           )
                   .first()
                   )
        if not user_id:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        operation = (
            self.session
            .query(Operation)
                .filter(Operation.id == operation_id,
                        Operation.user_id == user_id[0])


            .all()
        )
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return operation

    def _get(self, operation_id: int) -> Optional[Operation]:
        operation = (
            self.session
            .query(Operation)
            .filter(
                Operation.id == operation_id,
            )
            .first()
        )
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return operation
