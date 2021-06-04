from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    'postgresql://postgres:1234@localhost/postgres', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()