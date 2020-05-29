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

cursor.execute("DROP TABLE pizza")
db.commit()
cursor.execute("DROP TABLE pedido")
db.commit()
cursor.execute("DROP TABLE itens_pedido")
db.commit()
cursor.execute("DROP TABLE user")
db.commit()

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
               "item INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
               "id_ped INTEGER NOT NULL,"
               "id_pizza INTEGER,"
               "tamanho STRING (10),"
               "id_metade INTEGER,"
               "CONSTRAINT FK_ITENSPEDIDO_PEDI FOREIGN KEY(id_ped) REFERENCES pedido(id_ped),"
               "CONSTRAINT FK_ITENSPEDIDO_CODIGOPIZ FOREIGN KEY(id_pizza) REFERENCES pizza(id_pizza))")

db.commit()

cursor.execute("INSERT INTO pizza(data_criacao, nome_pizza, ingredientes, valor_custo) "
"VALUES(date('now', 'localtime'), 'ALHO E ÓLEO', 'Alho frito picado, parmesão ralado e azeitonas', '22.9'),"
"(date('now', 'localtime'), 'ALLICI', 'Alicci importado, rodelas de tomate, parmesão e azeitonas', '28.90'),"
"(date('now', 'localtime'), 'ATUM', 'Atum, cebola e azeitona', '22.9'),"
"(date('now', 'localtime'), 'BACON', 'Bacon coberto com muzzarela e azeitonas ', '26.90'),"
"(date('now', 'localtime'), 'BERINJELA', 'Berinjela, cobertura com muzzarela, manjericão e parmesão', '23.9'),"
"(date('now', 'localtime'), 'CAIPIRA', 'Frango desfiado, coberto com catupiry e milho verde e azeitonas', '26.90'),"
"(date('now', 'localtime'), 'CALABRESA', 'Linguiça calabresa, cebola e azeitonas ', '19.9'),"
"(date('now', 'localtime'), 'CINCO QUEIJOS', 'Muzzarela, parmesão, catupiry, gorgonzola e provolone', '29.9'),"
"(date('now', 'localtime'), 'ESCAROLA', 'Escarola refogada, muzzarela e azeitonas', '24.9'),"
"(date('now', 'localtime'), 'EXECUTIVA', 'Milho Verde, catupiry e azeitonas', '22.9'),"
"(date('now', 'localtime'), 'PERUANA', 'Atum, cebola, muzzarela e azeitonas', '26.9'),"
"(date('now', 'localtime'), 'PALMITO', 'Palmito com muzzarela e azeitonas', '26.9'),"
"(date('now', 'localtime'), 'BANANA', 'Banana fatiada com, cobertura com leite condensado e canela em pó', '21.9'),"
"(date('now', 'localtime'), 'BRIGADEIRO', 'Chocolate, leite condensado e chocolate granulado', '23.9'),"
"(date('now', 'localtime'), 'PRESTIGIO', 'Chocolate coberta com côco', '23.9')")

db.commit()