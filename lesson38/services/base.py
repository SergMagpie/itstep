from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'sqlite:///database.sqlite',
    connect_args={'check_same_thread': False},
    echo=False)

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

# Base = declarative_base()


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
