"""
Застосунок який дозволить фіксувати затрати та витрати 
і зберігати всі дані.

Що буде в застосунку, функціонал:
- додавати витрати та додавати дохід
- дані мають зберігатися в постійній пам'яті та я 
хочу мати доступ до них кожного разу коли використовую 
застосунок (використати БД)
- хочеться мати інтерфейс доступу та зміни даних

BL -> Bussines Logic
DB -> Database
I -> Inteface

SQLite/sqlalchemy

id, money_amount, date, reason, contragent
"""


from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.orm import validates

from datetime import date as d
from wallet.base import engine, Session, Base


# TODO перевірити від'ємні значення money_amount
# check None value to reason and contragent

class MoneyTable(Base):
    __tablename__ = "money_table"

    id = Column(Integer, primary_key=True)
    money_amount = Column(Numeric(12, 2))
    date = Column(Date)
    reason = Column(String)
    contragent = Column(String)

    def __init__(self,
                 money_amount,
                 date=d.today(),
                 reason=None,
                 contragent=None) -> None:
        self.money_amount = money_amount
        self.date = date
        self.reason = reason
        self.contragent = contragent

    def __str__(self) -> str:
        return (f"\nid {self.id}\n"
                f"money_amount {self.money_amount}\n"
                f"date {self.date}\n"
                f"reason {self.reason}\n"
                f"contragent {self.contragent}\n")

    def variables(self):
        return (self.id,
                self.money_amount,
                self.date,
                self.reason,
                self.contragent)

    @validates('date')
    def validate_date(self, key, value):
        if isinstance(value, d) and value <= d.today():
            return value
        else:
            return d.today()


if __name__ == "__main__":
    # generate tables in database
    Base.metadata.create_all(engine)

    # create session
    session = Session()

    # income = MoneyTable(1000,
    #                       d.today(),
    #                       reason="Test",
    #                       contragent="itstep")
    # outcome = MoneyTable(-500,
    #                       d.today(),
    #                       reason="Just for fun",
    #                       contragent="Me")
    none_val = MoneyTable(300, d.today())
    session.add(none_val)
    # session.add_all([income, outcome])
    # save data and close session
    session.commit()
    session.close()
