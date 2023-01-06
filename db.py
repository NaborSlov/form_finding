import os
from pathlib import Path

from tinydb import TinyDB

BASE_DIR = Path(__file__).resolve().parent

db = TinyDB(os.path.join(BASE_DIR, "db.json"))
forms = db.table("forms")
