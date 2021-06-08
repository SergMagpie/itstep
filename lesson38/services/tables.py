from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from services.base import engine, Session
from sqlalchemy.orm import foreign, remote
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)


class Operation(Base):
    __tablename__ = 'money_table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    money_amount = Column(Numeric(10, 2))
    date = Column(Date)
    reason = Column(String)
    contragent = Column(String, nullable=True)
    user = relationship("User",
                    primaryjoin=User.id == user_id)                
    # user = relationship('User')

Base.metadata.create_all(engine)
session = Session()
# create session
session.commit()
session.close()


#     # income = MoneyTable(1000,
#     #                       d.today(),
#     #                       reason="Test",
#     #                       contragent="itstep")
#     # outcome = MoneyTable(-500,
#     #                       d.today(),
#     #                       reason="Just for fun",
#     #                       contragent="Me")
#     none_val = MoneyTable(300, d.today())
#     session.add(none_val)
#     # session.add_all([income, outcome])
#     # save data and close session