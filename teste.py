import sqlite3

db = sqlite3.connect("database/pizza.db")

cursor = db.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#cursor.execute("INSERT INTO pessoas VALUES ('Maria', 10, 'teste@teste.com')")
#cursor.execute("SELECT * FROM user")
#print(cursor.fetchall())