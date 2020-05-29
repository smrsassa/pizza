import sqlite3
import include as inc


db = sqlite3.connect("database/pizza.db")

cursor = db.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#db.commit()
#cursor.execute("INSERT INTO pessoas VALUES ('Maria', 10, 'teste@teste.com')")
#db.commit()
#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

#import sys
#
#sys.path.insert(1, "..")
"""
import pandas as pd

lista = {'nome': ['samuel', 'maria'],
         'valor': [10, 20],
         'pizza': ['vinhedo', 'teste']}

listaDF = pd.DataFrame(lista)

print(listaDF)
"""