from sqlalchemy.sql.expression import desc
from money_table import MoneyTable
from base import engine, Session, Base
from datetime import date as d
# from sqlalchemy import update


class Wallet:

    def __init__(self) -> None:
        Base.metadata.create_all(engine)
        self.session = Session()

    def new_record(self,
                   money_amount,
                   date=d.today(),
                   reason=None,
                   contragent=None):
        record = MoneyTable(money_amount, date, reason, contragent)
        self.session.add(record)
        self.session.commit()

    def get_income(self, begin=None, end=None):
        """Метод повертає дохід.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount > 0)
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(
                MoneyTable).where(MoneyTable.date >= begin,
                                  MoneyTable.money_amount > 0)
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(
                MoneyTable).where(MoneyTable.date >= begin,
                                  MoneyTable.date <= end,
                                  MoneyTable.money_amount > 0)
        else:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount > 0)
        return result

    def get_outcome(self, begin=None, end=None):
        """Метод повертає затрати.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount < 0)
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(
                MoneyTable).where(MoneyTable.date >= begin,
                                  MoneyTable.money_amount < 0)
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(
                MoneyTable).where(MoneyTable.date >= begin,
                                  MoneyTable.date <= end,
                                  MoneyTable.money_amount < 0)
        else:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount < 0)
        return result

    def get_record_whith_id(self, id):
        result = self.session.query(MoneyTable).where(
            MoneyTable.id == id)
        return result

    def get_all_records(self, begin=None, end=None):
        """Метод повертає всі інвойси.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where()
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(MoneyTable).where(
                MoneyTable.date >= begin)
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(
                MoneyTable).where(MoneyTable.date >= begin,
                                  MoneyTable.date <= end)
        else:
            result = self.session.query(MoneyTable).where()
        return result

    def get_the_most_expensive_costs(self, begin=None, end=None):
        """Метод повертає всі інвойси, впорядковані по спаданню суми.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount < 0).order_by(
                MoneyTable.money_amount)
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(MoneyTable).where(
                MoneyTable.date >= begin,
                MoneyTable.money_amount < 0).order_by(
                    MoneyTable.money_amount)
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(MoneyTable).where(
                MoneyTable.date >= begin,
                MoneyTable.date <= end,
                MoneyTable.money_amount < 0).order_by(
                    MoneyTable.money_amount)
        else:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount < 0).order_by(
                MoneyTable.money_amount)
        return result

    def get_main_source_of_income(self, begin=None, end=None):
        """Метод повертає всі інвойси, впорядковані по спаданню суми.
            Якщо не вказано проміжок часу то повертається за увесь час.
            Якщо begin більше ніж end то змінити місцями"""
        if begin is None and end is None:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount > 0).order_by(
                desc(MoneyTable.money_amount))
        elif end is None and isinstance(begin, d):
            # validate date
            result = self.session.query(MoneyTable).where(
                MoneyTable.date >= begin,
                MoneyTable.money_amount > 0).order_by(desc(
                    MoneyTable.money_amount))
        elif isinstance(end, d) and isinstance(begin, d):
            if begin > end:
                begin, end = end, begin
            result = self.session.query(MoneyTable).where(
                MoneyTable.date >= begin,
                MoneyTable.date <= end,
                MoneyTable.money_amount > 0).order_by(desc(
                    MoneyTable.money_amount))
        else:
            result = self.session.query(MoneyTable).where(
                MoneyTable.money_amount > 0).order_by(
                desc(MoneyTable.money_amount))
        return result

    def update(self, id, new_value):
        self.session.query(MoneyTable).filter(
            MoneyTable.id == id).update(
            new_value, synchronize_session=False)
        self.session.commit()

    def close(self):
        self.session.close()

    def __del__(self):
        self.close()
