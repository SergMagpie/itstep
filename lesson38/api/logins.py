from fastapi import APIRouter, Depends, status
import models
from typing import List
from services import logins

router = APIRouter(
    prefix='/logins',
    tags=['logins']
)


@router.get(
    '/',
    response_model=List[models.ModelUser],
)
def get_all_users(
    operations_service: logins.Users = Depends(),
):
    """GET /logins - список усіх користувачів (усі логіни)"""
    return operations_service.get_all()


@router.post(
    '/',
    response_model=models.ModelUser,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    operation_data: models.UserCreate,
    operations_service: logins.Users = Depends(),
):
    return operations_service.create(
        operation_data,
    )
