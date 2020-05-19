import sqlite3


path = "database/pizza.db"

db = sqlite3.connect(path)

cursor = db.cursor()
