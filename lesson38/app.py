
from fastapi import FastAPI
from wallet.wallet import Wallet
from wallet.login import manager, query_user

app = FastAPI()
w = Wallet()

from fastapi import Depends
from starlette.responses import Response
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login.exceptions import InvalidCredentialsException


@app.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    return {'status': 'Success'}

@app.get('/auth')
def auth(response: Response, user=Depends(manager)):
    token = manager.create_access_token(
        data=dict(sub=user.email)
    )
    manager.set_cookie(response, token)
    return response


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/records")
def all_records():
    """GET /records - всі записи (список)"""
    return [r.__dict__ for r in w.get_all_records()]


@app.get("/records/{id}")
def records_id(id: int):
    """GET /records/<id> - конкретний запис, видається тільки у разі
    якщо власник запису та логін, що передається в запиті
    співпадає"""
    return [r.__dict__ for r in w.get_record_whith_id(id)]


@app.get("/incomes")
def income_records():
    """GET /incomes - список всіх записів з додатними значеннями"""
    return [r.__dict__ for r in w.get_income()]


@app.get("/outcomes")
def outcome_records():
    """GET /outcomes - список всіх записів з від'ємними
    значеннями"""
    return [r.__dict__ for r in w.get_outcome()]


"""
GET /logins - список усіх користувачів (усі логіни)
POST /records - створення нового запису
PATCH /records/<id> - зміна конкретного запису по id
DELETE /records/<id> - видалення конкретного запису по id
"""
