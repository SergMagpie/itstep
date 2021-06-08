from datetime import date as d
import requests
# import json
# response = requests.get("http://127.0.0.1:8000/records")
# print(response.json())


class Wallet:

    # def __init__(self) -> None:

    def new_record(self,
                   user_id,
                   money_amount,
                   date=d.today(),
                   reason=None,
                   contragent=None):
        """Add new record"""
        result = requests.post("http://127.0.0.1:8000/records/",
                               json={
                                   "user_id": str(user_id),
                                   "money_amount": str(money_amount),
                                   "date": str(date),
                                   "reason": reason,
                                   "contragent": contragent
                               }
                               ).json()
        print(result)

    def get_income(self, begin=None, end=None):
        """Метод повертає дохід."""
        result = requests.get("http://127.0.0.1:8000/incomes",
                              params={'begin': begin, 'end': end}).json()
        return result

    def get_outcome(self, begin=None, end=None):
        """Метод повертає затрати."""
        result = requests.get("http://127.0.0.1:8000/outcomes",
                              params={'begin': begin, 'end': end}).json()
        return result

    # def get_record_whith_id(self, id):
    #     result = self.session.query(MoneyTable).where(
    #         MoneyTable.id == id)
    #     return result

    def get_all_records(self, begin=None, end=None):
        """Метод повертає всі інвойси"""
        result = requests.get("http://127.0.0.1:8000/records",
                              params={'begin': begin, 'end': end}).json()
        return result

    def get_all_users(self):
        """Метод повертає всі інвойси"""
        result = requests.get("http://127.0.0.1:8000/logins"
                              ).json()
        return result

    def update(self,
               id,
               user_id,
               money_amount,
               date=d.today(),
               reason=None,
               contragent=None):
        result = requests.patch(f"http://127.0.0.1:8000/records/{id}",
                                json={
                                    "user_id": str(user_id),
                                    "money_amount": str(money_amount),
                                    "date": str(date),
                                    "reason": reason,
                                    "contragent": contragent
                                }
                                ).json()
        print(result)

    def delete(self, id):
        result = requests.delete(f"http://127.0.0.1:8000/records/{id}")
        print(result)
