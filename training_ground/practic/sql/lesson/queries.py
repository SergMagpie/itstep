from singer import Singer
from datetime import date
from base import Session
from colorama import Fore, Back, Style

session = Session()


singers = session.query(Singer).all()


for s in singers:
    print(f"{Fore.RED}Singer {s.nickname} was released in {s.released_at}")
print(Style.RESET_ALL)

singers_before_2000 = session.query(Singer).filter(Singer.released_at < date(1999, 12, 31)).limit(2)

print("SINGERS BEFORE 2000")
for s in singers_before_2000:
    print(f"{Fore.RED}Singer {s.nickname} was released in {s.released_at}")
print(Style.RESET_ALL)

singers_count = session.query(Singer).filter(Singer.released_at < date(2010, 1, 1)).count()
print(singers_count)
session.close()