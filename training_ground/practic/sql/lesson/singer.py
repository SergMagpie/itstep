from sqlalchemy import Column, Integer, String, Date

from datetime import date
from base import Base


class Singer(Base):
    __tablename__ = "singers"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    released_at = Column(Date)

    def __init__(self, nickname, released=date.today()) -> None:
        self.nickname = nickname
        self.released_at = released
