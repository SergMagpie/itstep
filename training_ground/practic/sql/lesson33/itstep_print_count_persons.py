from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)

db = client['itstep']

students = db['persons']

number = students.count_documents({"wallet.uah": {"$gt": 1000}})

print(number)
