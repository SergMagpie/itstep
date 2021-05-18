from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from sqlalchemy.orm import relationship
from base import Base


class Processor(Base):
    __tablename__ = "processor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(32))
    number_of_cores = Column('number_of_cores', Integer)
    clock_speed = Column('clock_speed', Numeric)
    manufacturer = Column('manufacturer', String(32))
    children = relationship("Phone", back_populates="parent")

    def __init__(self,
                 name,
                 number_of_cores,
                 clock_speed,
                 manufacturer) -> None:
        # super().__init__()
        self.name = name
        self.number_of_cores = number_of_cores
        self.clock_speed = clock_speed
        self.manufacturer = manufacturer

    def __str__(self) -> str:
        return (f"\nid {self.id}\n"
                f"name {self.name}\n"
                f"number of cores {self.number_of_cores}\n"
                f"clock speed {float(self.clock_speed)}\n"
                f"manufacturer {self.manufacturer}\n")
