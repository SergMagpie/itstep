from sqlalchemy.orm.session import sessionmaker
from base import engine, Session, Base
from pet import Pet
from datetime import date


Base.metadata.create_all(engine)

session = Session()

parrot = Pet(nickname="Kesha", age=2, species_of_animal='Parrot')
cat = Pet(nickname="Murka", age=5, species_of_animal='Cat')
fish = Pet(nickname="Golden", age=1, species_of_animal='Fish')
dog = Pet(nickname="Jimm", age=8, species_of_animal='Dog')
snail = Pet(nickname="Harry", age=5, species_of_animal='Snail')

session.add_all([parrot, cat, fish, dog, snail])


session.commit()
session.close()