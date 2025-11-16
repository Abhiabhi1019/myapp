import json
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/mydatabase")
client = MongoClient(MONGO_URI)

db = client["mydatabase"]
collection = db["items"]   # or whatever your collection name is

with open("/app/mongo_seed/sample.json", "r") as f:
    data = json.load(f)

if isinstance(data, list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Seed data inserted successfully!")
