"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
Descrição..: Esse arquivo contem funções que realizam updates no banco
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


def up_usuario(id_cliente, tel_fixo, tel_cel, nome_cli, endereco, nr_end, complemento, bairro, cidade, uf, cep):
    data.cursor.execute("UPDATE user "
                        "SET tel_fixo = '{}',"
                        "tel_cel = '{}',"
                        "nome_cli = '{}',"
                        "endereco = '{}',"
                        "nr_end = '{}',"
                        "complemento = '{}',"
                        "bairro = '{}',"
                        "cidade = '{}',"
                        "uf = '{}',"
                        "cep = '{}' "
                        "WHERE id_user = '{}'".format(tel_fixo, tel_cel, nome_cli, endereco,
                                                    nr_end, complemento, bairro, cidade,
                                                    uf, cep, id_cliente))

    data.db.commit()
