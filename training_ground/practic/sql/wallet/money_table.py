"""
App for fix invoices

- add costs and revenues
- the data must be stored in non-volatile memory
- data access and change interface

BL -> Bussines Logic
DB -> Database
I -> Interface

MVC -> Model-View-Controller

SQLite/sqlalchemy

id, money_amount, date, reason, contragent
"""

from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Numeric, Date
from sqlalchemy.orm import relationship, validates
from base import Base, engine, Session, Base
from datetime import date as d

# TODO check the negative values of the money_amount

class MoneyTable(Base):
    __tablename__ = "money_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    money_amount = Column('money_amount', Numeric)
    date = Column('date', Date)
    reason = Column('reason', String(64))
    contragent = Column('contragent', String(64))


    def __init__(self,
                 money_amount,
                 date=d.today(),
                 reason=None,
                 contragent=None) -> None:
        # super().__init__()
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

    @validates('date')
    def validates_date(self, key, value):
        pass

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    session = Session()

    income = MoneyTable(1000, d.today(), "test", "itstep")
    outcome = MoneyTable(-500, d.today(), "Just for fun", "Me")
    empty = MoneyTable(500)
    session.add_all([income, outcome, empty])


    session.commit()
    session.close()