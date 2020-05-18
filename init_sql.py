"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
Descrição..: Esse arquivo tem o objetivo de criar todo o banco de dados.
Basta rodar esse arquivo e seu banco vai estar pronto para uso.
"""
import sqlite3

db = sqlite3.connect("database/pizza.db")

cursor = db.cursor()

#cursor.execute("DROP TABLE pizza")
#db.commit()
#cursor.execute("DROP TABLE pedido")
#db.commit()
#cursor.execute("DROP TABLE itens_pedido")
#db.commit()

cursor.execute("CREATE TABLE user("
               "id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
               "tel_fixo STRING (15),"
               "tel_cel STRING (15),"
               "nome_cli STRING (40),"
               "endereco STRING (30),"
               "nr_end STRING (10),"
               "complemento STRING (25),"
               "bairro STRING (20),"
               "cidade STRING (20),"
               "uf STRING (02),"
               "cep STRING (10))")
db.commit()

cursor.execute("CREATE TABLE pizza("
               "id_pizza INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
               "data_criacao DATE,"
			   "data_inativacao DATE,"
			   "nome_pizza STRING (100),"
			   "ingredientes TEXT,"
			   "valor_custo NUMERIC(10,2))")

db.commit()

cursor.execute("CREATE TABLE pedido("
               "id_ped INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
               "data_ped DATE,"
               "hora_ped TIME,"
               "id_user INTEGER,"
               "total_ped NUMERIC(10,2),"
               "CONSTRAINT FK_PEDIDO_CODIGOCLI FOREIGN KEY(id_user) REFERENCES user(id_user))")

db.commit()

cursor.execute("CREATE TABLE itens_pedido("
               "id_ped INTEGER NOT NULL,"
               "item INTEGER NOT NULL,"
               "id_pizza INTEGER,"
               "tamanho STRING (10),"
               "CONSTRAINT PK_ITENSPEDIDO PRIMARY KEY(id_ped, item),"
               "CONSTRAINT FK_ITENSPEDIDO_CODIGOPIZ FOREIGN KEY(id_pizza) REFERENCES pizza(id_pizza))")

db.commit()