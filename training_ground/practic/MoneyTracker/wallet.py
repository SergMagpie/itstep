from money_table import MoneyTable
from base import engine, Session, Base
from datetime import date as d


class Wallet:

    def __init__(self) -> None:
        Base.metadata.create_all(engine)
        self.session = Session()
        
    def new_record(self, money_amount, date=d.today(), reason=None, contragent=None):
        record = MoneyTable(money_amount, date, reason, contragent)
        self.session.add(record)
        self.session.commit()

    def get_income(self, begin=None, end=None):
        """Метод повертає дохід.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where(MoneyTable.money_amount > 0)
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(MoneyTable).where(MoneyTable.date >= begin, 
                                                          MoneyTable.money_amount > 0)
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(MoneyTable).where(MoneyTable.date >= begin, 
                                                          MoneyTable.date <= end, 
                                                          MoneyTable.money_amount > 0)
        else:
            result = self.session.query(MoneyTable).where(MoneyTable.money_amount > 0)
        return result
    
    def get_outcome(self, begin=None, end=None):
        """Метод повертає затрати.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where(MoneyTable.money_amount < 0)
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(MoneyTable).where(MoneyTable.date >= begin, 
                                                          MoneyTable.money_amount < 0) 
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(MoneyTable).where(MoneyTable.date >= begin, 
                                                          MoneyTable.date <= end, 
                                                          MoneyTable.money_amount < 0)
        else:
            result = self.session.query(MoneyTable).where(MoneyTable.money_amount < 0)
        return result

    def get_all_records(self):
        return self.session.query(MoneyTable).where()
    
    def update(self, id, new_value):
        # need to be realised
        pass

    def close(self):
        self.session.close()
    
    def __del__(self):
        self.close()