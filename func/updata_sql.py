"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
"""
import database.db as data


def up_pizza(id, nome_pizza, ingredientes, custo):
    data.cursor.execute("UPDATE pizza "
                        "SET nome_pizza = '{}',"
                            "ingredientes = '{}',"
                            "valor_custo = '{}' "
                        "WHERE id_pizza = '{}'".format(nome_pizza, ingredientes, custo, id))
    data.db.commit()


def invalidar_pizza(id_pizza):
    data.cursor.execute("UPDATE pizza "
                        "SET data_inativacao = date('now', 'localtime') "
                        "WHERE id_pizza = '{}'".format(id_pizza))
    data.db.commit()
