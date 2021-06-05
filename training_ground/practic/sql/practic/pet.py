from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Date, Integer, String
from datetime import date
from base import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    age = Column(Integer)
    species_of_animal = Column(String)

    def __init__(self, nickname, age, species_of_animal) -> None:
        # super().__init__()
        self.nickname = nickname
        self.age = age
        self.species_of_animal = species_of_animal
        pass

