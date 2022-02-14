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


doc = db.pytech.find_one({"student_id": "1007"})

print(doc["student_id"])