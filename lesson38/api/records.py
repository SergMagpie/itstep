from fastapi import APIRouter, Depends, status, Response
import models
from typing import List
from services import operations
from datetime import date

router = APIRouter(
    prefix='/records',
    tags=['records']
)


@router.get(
    '/',
    response_model=List[models.Operation],
)
def get_all(
    operations_service: operations.Operations = Depends(),
    begin: date = None,
    end: date = None,
):
    """GET /records - всі записи (список)"""
    return operations_service.get_all(begin, end)


@router.get(
    '/{operation_id}',
    response_model=List[models.Operation],
)
def get_id(
    operation_id: int,
    username: str,
    password: str,
    operations_service: operations.Operations = Depends()):
    """GET /records - всі записи (список)"""
    return operations_service.get_id(operation_id, username, password)


@router.post(
    '/',
    response_model=models.Operation,
    status_code=status.HTTP_201_CREATED,
)
def create_operation(
    operation_data: models.OperationCreate,
    operations_service: operations.Operations = Depends(),
):
    return operations_service.create(
        operation_data,
    )


@router.patch(
    '/{operation_id}',
    response_model=models.Operation,
)
def update_operation(
    operation_id: int,
    operation_data: models.OperationCreate,
    operations_service: operations.Operations = Depends(),
):
    """PATCH /records/<id> - зміна конкретного запису по id"""
    return operations_service.update(
        operation_id,
        operation_data,
    )


@router.delete(
    '/{operation_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_operation(
    operation_id: int,
    operations_service: operations.Operations = Depends(),
):
    """DELETE /records/<id> - видалення конкретного запису по id"""
    operations_service.delete(
        operation_id,
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
