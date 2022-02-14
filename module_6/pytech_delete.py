from pymongo import MongoClient

try: 
    client = MongoClient('localhost', 27017)
    print("Connected Successfully!")

except: 
    print("Could not connect")

db = client['pytech']

docs = db.pytech.find({})

for doc in docs:
    print(doc)

student_1 = {
    "name":"Robert",
    "student_id":"1010"
}

insert_1 = db.pytech.insert_one(student_1)

find = db.pytech.find_one({"student_id": "1010"})

print(find["student_id"])

delete = db.pytech.delete_one({"student_id": "1010"})

for doc in docs:
    print(doc)