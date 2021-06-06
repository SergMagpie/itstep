from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import settings

engine = create_engine(settings.database_url, 
    echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
