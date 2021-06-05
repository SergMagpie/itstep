from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from sqlalchemy.orm import relationship
from base import Base


class Phone(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_manufacturer = Column('manufacturer', String(32))
    model = Column('model', String(64))
    diagonal = Column('diagonal', Numeric)
    price = Column('price', Numeric)
    processor = Column(Integer, ForeignKey('processor.id'))
    parent = relationship("Processor", back_populates="children")

    def __init__(self,
                 company_manufacturer,
                 model,
                 diagonal,
                 price,
                 processor) -> None:
        # super().__init__()
        self.company_manufacturer = company_manufacturer
        self.model = model
        self.diagonal = diagonal
        self.price = price
        self.processor = processor

    def __str__(self) -> str:
        return (f"\nid {self.id}\n"
                f"manufacter {self.company_manufacturer}\n"
                f"model {self.model}\n"
                f"diagonal {float(self.diagonal)}\n"
                f"price {float(self.price)}\n"
                f"processor {self.processor}\n")
