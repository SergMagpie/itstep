from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.orm import validates

from datetime import date as d
from base import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer)
    user_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    date = Column(Date)
    text = Column(String)

    def __init__(self,
                 message) -> None:
        self.message_id = message.id
        self.user_id = message.from_user.id
        self.first_name = message.from_user.first_name
        self.last_name = message.from_user.last_name
        self.date = d.fromtimestamp(message.date)
        self.text = message.text

    def __str__(self) -> str:
        return (f"\nid {self.id}\n"
                f"message_id {self.message_id}\n"
                f"user_id {self.user_id}\n"
                f"first_name {self.first_name}\n"
                f"last_name {self.last_name}\n"
                f"date {self.date}\n"
                f"text {self.text}\n")

    def items(self):
        return {"message_id": self.message_id,
                "user_id": self.user_id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "date": self.date,
                "text": self.text}

    # def variables(self):
    #     return (self.id,
    #             self.money_amount,
    #             self.date,
    #             self.reason,
    #             self.contragent)

    # @validates('date')
    # def validate_date(self, key, value):
    #     if isinstance(value, d) and value <= d.today():
    #         return value
    #     else:
    #         return d.today()


# if __name__ == "__main__":
    # import json, os
    # abspath = os.path.abspath(__file__)
    # dname = os.path.dirname(abspath)
    # file_name = os.path.join(dname, "message")
    # with open(file_name, "r") as f:
    #     message = json.load(f)
    # generate tables in database
    # Base.metadata.create_all(engine)
    # # create session
    # session = Session()
    # # m = Messages(message)
    # # session.add(m)
    # # session.add_all([income, outcome])
    # # # save data and close session
    # # print(*m)
    # session.commit()
    # session.close()
