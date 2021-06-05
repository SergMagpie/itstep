from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Date, Integer, String
from datetime import date
from base import Base

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    released_at = Column(Date)

    def __init__(self, nicname, released_at=date.today()) -> None:
        # super().__init__()
        self.nicname = nicname
        self.released_at = released_at
        pass

