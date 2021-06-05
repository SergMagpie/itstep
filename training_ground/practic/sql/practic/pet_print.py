from pet import Pet
from datetime import date
from base import Session
from colorama import Fore, Back, Style

session = Session()


pets = session.query(Pet).all()


for s in pets:
    print(f"{Fore.RED}Pet {s.nickname} is {str(s.age)} ears old is {s.species_of_animal}")
print(Style.RESET_ALL)

spec = input('species_of_animal ')

specials = session.query(Pet).filter(Pet.species_of_animal == spec)

for s in specials:
    print(f"{Fore.RED}Pet {s.nickname} is {str(s.age)} ears old is {s.species_of_animal}")
print(Style.RESET_ALL)

session.close()