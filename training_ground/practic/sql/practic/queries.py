from artist import Singer
from datetime import date
from base import Session
from colorama import Fore, Back, Style

session = Session()

singers = session.query(Singer).all()

singers_before_2000 = session.query(Singer).filter(singer.released_at < date(2010, 1, 1)).exist()

print("SINGERS BEFORE 2000")
for s in singers_before_2000: