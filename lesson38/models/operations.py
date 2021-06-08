from datetime import date
from decimal import Decimal
from typing import Optional
from models.logins import BaseUser
from pydantic import BaseModel


class BaseOperation(BaseModel):    
    user_id: int
    money_amount: Decimal
    date: date
    reason: Optional[str]
    contragent: Optional[str]


class OperationCreate(BaseOperation):
    pass


class OperationUpdate(BaseOperation):
    pass


class Operation(BaseOperation):
    id: int

    class Config:
        orm_mode = True
