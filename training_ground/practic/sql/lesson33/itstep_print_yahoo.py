from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)

db = client['itstep']

students = db['persons']

all = students.find({"Company": "Yahoo"})

for student in all:
    pprint(student, sort_dicts=False)
