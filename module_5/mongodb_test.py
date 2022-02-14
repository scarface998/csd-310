from http import client
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.01va3.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names)