# import os, psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

engine = create_engine(
    'postgresql+psycopg2://zcourfhxzgmneq:25d14d265e20be7ba29c3e7c8d34d7ab3e1015bfbbadd09dddf8700fd0ac0f43@ec2-52-17-1-206.eu-west-1.compute.amazonaws.com:5432/d291rtonnnc4pt', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()