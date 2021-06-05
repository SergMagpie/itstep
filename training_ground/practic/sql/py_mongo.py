from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['students']

students = db['students'] # db['singers']

students.insert_one({"name": "Petro", 
                    "suname" : "Vasin", 
                    "birsday": "17/05/2021",
                    "graduates" : 5})

all = students.find()

for student in all:
    print(student)