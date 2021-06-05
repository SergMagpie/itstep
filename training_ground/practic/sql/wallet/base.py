from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from sqlalchemy import event

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

engine = create_engine('sqlite:///wallet.sqlite', echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


event.listen(engine, 'connect', _fk_pragma_on_connect)
