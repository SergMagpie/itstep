
from fastapi import FastAPI
from wallet.wallet import Wallet

app = FastAPI()
w = Wallet()


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
