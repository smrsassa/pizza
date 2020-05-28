"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
"""
import database.db as data
import func.msg as msg


def in_user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep):
    data.cursor.execute('INSERT INTO user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep) '
                        'VALUES (?,?,?,?,?,?,?,?,?,?)',
            (tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep))
    data.db.commit()

def in_pizza():
    data.cursor.execute("SELECT * FROM pessoas")
    print(data.cursor.fetchall())
#data_criacao,data_inativacao,nome_pizza,ingredientes,valor_custo

def in_pedido(id_user, total):
    data.cursor.execute("INSERT INTO pedido(data_ped, hora_ped, id_user, total_ped)"
                        "VALUES (date('now', 'localtime'), time('now', 'localtime'), {}, {})".format(id_user, total))
    data.db.commit()
#data_ped,hora_ped,id_user,total_ped

def in_itens_ped(id_ped, id_pizza, tamanho):
    data.cursor.execute("INSERT INTO itens_pedido(id_ped, id_pizza, tamanho)"
                        "VALUES ({}, {}, {})".format(id_ped, id_pizza, tamanho))
    data.db.commit()
#id_pizza,tamanho

def fechando_pedido(pizzas, tamanhos, cliente):
    valor_total = 0
    contador = 0
    for value in range(0, len(pizzas)):
        contador += 1
        data.cursor.execute("SELECT valor_custo FROM pizza WHERE id_pizza = {}".format(pizzas[value]))
        total = data.cursor.fetchall()
        total = int(total[0][0])
        if int(tamanhos[value][0]) == 2:
            total = total * 1.15
        elif int(tamanhos[value][0]) == 3:
            total = total * 1.25
        elif int(tamanhos[value][0]) == 4:
            total = total * 1.35

        valor_total += total

        import datetime
        data_hora = datetime.datetime.now()
        data_hora = data_hora.strftime('%d/%m/%Y %H %M')
        hora = data_hora.split()
        a1 = datetime.datetime(100, 1, 1, int(hora[1]), int(hora[2]))
        a = a1 + datetime.timedelta(0, 3000)
        a = str(a)
        a = a.split()
        data_hora = data_hora.split()
        a1 = str(a1).split()
        #a[1], a1[1], data_hora[0]

        if contador == 1:
            in_pedido(cliente, 0)

        data.cursor.execute("SELECT id_ped FROM pedido ORDER BY id_ped DESC LIMIT 1")
        id_pedido = data.cursor.fetchall()
        in_itens_ped(id_pedido[0][0], pizzas[value], tamanhos[value])

    data.cursor.execute("UPDATE pedido SET total_ped = {} WHERE id_ped = {} ".format(valor_total, id_pedido[0][0]))
    data.db.commit()

    #Estou fazendo isso pq o format tem um limite de tamanho :(
    string1 = "WHERE pedido.id_ped = '{}' AND itens_pedido.id_ped = pedido.id_ped ".format(id_pedido[0][0])
    string2 = " AND user.id_user = '{}'".format(cliente)
    string = string1 + string2
    data.cursor.execute("SELECT pedido.id_ped, pedido.data_ped, user.NOME_CLI, pedido.total_ped "
                        "FROM pedido, itens_pedido, user " + string)
    rela = data.cursor.fetchall()

    data.cursor.execute("SELECT pizza.nome_pizza "
                        "FROM itens_pedido, pizza "
                        "WHERE itens_pedido.id_pizza = pizza.id_pizza and itens_pedido.id_ped = {}".format(id_pedido[0][0]))
    pizzas = data.cursor.fetchall()

    print("|" + "==" * 19 + "|")
    print("| Numero do pedido: {}".format(rela[0][0]))
    print("| Data: {}".format(rela[0][1]))
    print("| Cliente: {}".format(rela[0][2]))
    print("| Total: R${}".format(rela[0][3]))
    print("| Pizzas: ")
    for item in pizzas:
        print("| - {}".format(item[0]))
    print("|" + "==" * 19 + "|")
