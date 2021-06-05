from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref

from datetime import date

from base import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    released_at = Column(Date)
    duration = Column(Integer)
    genre = Column(String)
    singer_id = Column(Integer, ForeignKey('singers.id'))
    singer = relationship("Singer", backref=backref("tracks"))

    def __init__(self, name, duration, genre, singer, released_at=date.today()) -> None:
        self.name = name
        self.duration = duration
        self.genre = genre
        self.singer = singer
        self.released_at = released_at
        