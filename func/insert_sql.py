"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
Descrição..: Esse arquivo contem funções que realizam inserts no banco
"""
import database.db as data


def in_user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep):
    data.cursor.execute('INSERT INTO user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep) '
                        'VALUES (?,?,?,?,?,?,?,?,?,?)',
            (tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep))
    data.db.commit()

def in_pedido(id_user, total):
    data.cursor.execute("INSERT INTO pedido(data_ped, hora_ped, id_user, total_ped)"
                        "VALUES (date('now', 'localtime'), time('now', 'localtime'), {}, {})".format(id_user, total))
    data.db.commit()
#data_ped,hora_ped,id_user,total_ped

def in_itens_ped(id_ped, id_pizza, tamanho, id_matade):
    data.cursor.execute("INSERT INTO itens_pedido(id_ped, id_pizza, tamanho, id_metade)"
                        "VALUES ({}, {}, {}, {})".format(id_ped, id_pizza, tamanho, id_matade))
    data.db.commit()
#id_pizza,tamanho

def fechando_pedido(pizzas, tamanhos, cliente, id_metade):
    contador = 0
    valor_total = 0
    for value in range(0, len(pizzas)):
        contador += 1
        data.cursor.execute("SELECT valor_custo FROM pizza WHERE id_pizza = {}".format(pizzas[value]))
        totala = data.cursor.fetchall()
        total = int(totala[0][0])
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
        in_itens_ped(id_pedido[0][0], pizzas[value], tamanhos[value], id_metade[value])

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
                        "WHERE itens_pedido.id_pizza = pizza.id_pizza and "
                        "itens_pedido.id_ped = {} or "
                        "itens_pedido.id_metade = pizza.id_pizza and "
                        "itens_pedido.id_ped = {}".format(id_pedido[0][0], id_pedido[0][0]))
    pizzas = data.cursor.fetchall()

    opc_pagamento = int(input("| [1] Sim\n"
                          "| [2] Não\n"
                          "| Vai pagar com cartão? "))

    while True:
        if opc_pagamento == 1:
            troco = 0
            break
        else:
            valor = int(input("| Ex: 50\n"
                              "| Qual o valor total das notas do cliente: "))
            troco = valor - rela[0][3]
            break

    print("|" + "==" * 19 + "|")
    print("| Numero do pedido: {}".format(rela[0][0]))
    print("| Data: {}".format(rela[0][1]))
    print("| Cliente: {}".format(rela[0][2]))
    print("| Total: R${:0.2f}".format(rela[0][3]))
    print("| Troco: R${:0.2f}".format(troco))
    print("| Pizzas: ")
    for item in pizzas:
        print("| - {}".format(item[0]))
    print("|" + "==" * 19 + "|")
    getchar = input("Aperte Enter para continuar...")


def in_pizza(nome_pizza, ingredientes, custo):
    data.cursor.execute("INSERT INTO pizza(data_criacao,nome_pizza,ingredientes,valor_custo) "
                        "VALUES (date('now', 'localtime'),'{}','{}','{}')".format(nome_pizza, ingredientes, custo))
    data.db.commit()
