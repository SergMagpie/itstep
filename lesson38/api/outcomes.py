from fastapi import APIRouter, Depends, status
import models
from typing import List
from services import operations
from datetime import date

router = APIRouter(
    prefix='/outcomes',
    tags=['outcomes']
)


@router.get(
    '/',
    response_model=List[models.Operation],
)
def get_incomes(
    operations_service: operations.Operations = Depends(),
    begin: date = None,
    end: date = None,
):
    """GET /incomes - список всіх записів з додатними значеннями"""
    return operations_service.get_outcomes(begin, end)
