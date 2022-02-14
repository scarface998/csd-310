from sqlite3 import connect
from sys import set_asyncgen_hooks
from pymongo import MongoClient

try: 
    client = MongoClient('localhost', 27017)
    print("Connected Successfully!")

except: 
    print("Could not connect")

db = client['pytech']

collection = db['students']

student_1 = {
    "name":"Robert",
    "student_id":"1007"
}

student_2 = {
    "name":"Jim",
    "student_id":"1008"
}

student_3 = {
    "name":"Dave",
    "student_id":"1009"
}

insert_1 = collection.insert_one(student_1)
insert_2 = collection.insert_one(student_2)
insert_3 = collection.insert_one(student_3)

print("Data inserted")

cursor = collection.find()
for record in cursor:
    print(record)