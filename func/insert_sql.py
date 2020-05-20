import database.db as data


def in_user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep):
    data.cursor.execute('INSERT INTO user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep) '
                        'VALUES (?,?,?,?,?,?,?,?,?,?)',
            (tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep))
    data.db.commit()

def in_pizza():
    data.cursor.execute("SELECT * FROM pessoas")
    print(data.cursor.fetchall())
#data_criacao,data_inativacao,nome_pizza,ingredientes,valor_custo

def in_pedido():
    data.cursor.execute("SELECT * FROM pessoas")
    print(data.cursor.fetchall())
#data_ped,hora_ped,id_user,total_ped

def in_itens_ped():
    data.cursor.execute("SELECT * FROM pessoas")
    print(data.cursor.fetchall())
#id_pizza,tamanho