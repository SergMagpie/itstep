from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['itstep']

students = db['persons']

students_list = [
    {"firstName": "John",
     "lastName": "West",
     "email": "john.west@mail.com",
     "phone": "032345432134",
     "wallet": {"eur": 20,
                "usd": 30,
                "uah": 20000},
     "address": {
         "building": "1007",
         "city": "New York",
         "street": "Morris Park Ave",
         "zipcode": "10462"
     },
        "Company": "Coca-Cola"},
    {"firstName": "Piter",
     "lastName": "Pen",
     "email": "piter.pen@gmail.com",
     "phone": "032445832135",
     "wallet": {"eur": 30,
                "usd": 40,
                "uah": 200},
     "address": {
         "building": "1070",
         "city": "St. Pitersburg",
         "street": "Admirala Naghimova",
         "zipcode": "10488"
     },
        "Company": "Roshen"},
    {"firstName": "Diana",
     "lastName": "Ross",
     "email": "diana.ross@mail.com",
     "phone": "085691215341",
     "wallet": {"eur": 60,
                "usd": 20,
                "uah": 10000},
     "address": {
         "building": "8807",
         "city": "New Vasuki",
         "street": "Dudaeva street",
         "zipcode": "45862"
     },
        "Company": "NASA"},
    {"firstName": "Mark",
     "lastName": "Tsukerberg",
     "email": "mark.tsuk@gmail.com",
     "phone": "045612312314",
     "wallet": {"eur": 90,
                "usd": 80,
                "uah": 500},
     "address": {
         "building": "4567",
         "city": "New York",
         "street": "Presidentskaya",
         "zipcode": "45678"
     },
        "Company": "Yahoo"},
    {"firstName": "Rebekka",
     "lastName": "Berlington",
     "email": "rebe.bell@mail.com",
     "phone": "045612335474",
     "wallet": {"eur": 40,
                "usd": 10,
                "uah": 10000},
     "address": {
         "building": "4547",
         "city": "Loss Angeless",
         "street": "Palm Beach",
         "zipcode": "85214"
     },
        "Company": "Samsung electronics"},
]

students.insert_many(students_list)
