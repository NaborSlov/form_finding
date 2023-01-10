import pymongo

client = pymongo.MongoClient("mongodb://username:hard_password@mongo:27017")
db = client["my_db"]
collection = db["forms"]
