from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///database.sqlite', echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()
