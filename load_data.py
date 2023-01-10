import json

from db import collection, client

requesting = []
with open(r"db.json") as f:
    myDict: dict[str, dict] = json.load(f)["forms"]

    for jsonObj in myDict.values():
        collection.insert_one(jsonObj)
client.close()
