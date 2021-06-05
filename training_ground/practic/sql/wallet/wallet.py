from money_table import MoneyTable
from base import Base, engine, Session, Base

class Wallet:

    def __init__(self) -> None:
        Base.metadata.create_all(engine)
        self.session = Session()

    def new_record(self,
                 money_amount,
                 date,
                 reason,
                 contragent):
        pass

    def get_income(self, begin=None, end=None):
        pass


    pass
