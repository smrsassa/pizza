import database.db as data

#====== Atendimento =================================================
def procura_cliente(tel):
    data.cursor.execute('SELECT * from user WHERE tel_cel like "%{}%"'.format(tel))
    num_row = data.cursor.fetchone()
    if num_row is None:
        return False
    else:
        return num_row[0]

#====== Pedidos =================================================
def pedidos_aberto():
    import pandas as pd

    data.cursor.execute("SELECT pedido.id_ped, user.NOME_CLI, pedido.hora_ped, pedido.total_ped, "
                        "pizza.nome_pizza, itens_pedido.tamanho FROM pedido, user, pizza, itens_pedido "
                        "WHERE pedido.data_ped = date('now', 'localtime') AND pedido.id_ped = itens_pedido.id_ped AND "
                        "pedido.id_user = user.id_user AND itens_pedido.id_pizza = pizza.id_pizza")
    rows = data.cursor.fetchall()
    id_ped = []
    nome = []
    hora = []
    total = []
    pizza = []
    tamanho = []
    for row in rows:
        id_ped.append(row[0])
        nome.append(row[1])
        hora.append(row[2])
        total.append("R$" + str(row[3]))
        pizza.append(row[4])
        if row[5] == 1:
            tam = "normal"
        elif row[5] == 2:
            tam = "Media"
        elif row[5] == 3:
            tam = "Grando"
        elif row[5] == 4:
            tam = "Gigante"
        tamanho.append(tam)

    pedidosDIC = {'Pedido': id_ped,
                  'Cliente': nome,
                  'Hora Pedido': hora,
                  'Valor': total,
                  'Pizza': pizza,
                  'Tamanho': tamanho}

    pedidosDF = pd.DataFrame(pedidosDIC)

    print(pedidosDF)

    getChar = input("Aperte Enter para continuar...")


#print(titulo.center(50))
def ultimos_pedidos(data_asd):
    import pandas as pd
    where = "WHERE pedido.data_ped = '{}' AND pedido.id_ped = itens_pedido.id_ped AND ".format(data_asd)
    data.cursor.execute("SELECT pedido.id_ped, user.NOME_CLI, pedido.hora_ped, pedido.total_ped, "
                        "pizza.nome_pizza, itens_pedido.tamanho FROM pedido, user, pizza, itens_pedido "
                        + where +
                        "pedido.id_user = user.id_user AND itens_pedido.id_pizza = pizza.id_pizza")
    rows = data.cursor.fetchall()
    id_ped = []
    nome = []
    hora = []
    total = []
    pizza = []
    tamanho = []
    for row in rows:
        id_ped.append(row[0])
        nome.append(row[1])
        hora.append(row[2])
        total.append("R$" + str(row[3]))
        pizza.append(row[4])
        if row[5] == 1:
            tam = "normal"
        elif row[5] == 2:
            tam = "Media"
        elif row[5] == 3:
            tam = "Grando"
        elif row[5] == 4:
            tam = "Gigante"
        tamanho.append(tam)

    pedidosDIC = {'Pedido': id_ped,
                  'Cliente': nome,
                  'Hora Pedido': hora,
                  'Valor': total,
                  'Pizza': pizza,
                  'Tamanho': tamanho}

    pedidosDF = pd.DataFrame(pedidosDIC)

    print(pedidosDF)

    getChar = input("Aperte Enter para continuar...")

#====== Produtos =================================================
def vendas():
    import pandas as pd
    data.cursor.execute("SELECT pizza.nome_pizza, count(itens_pedido.id_pizza) as vendas "
                        "FROM itens_pedido, pizza "
                        "WHERE itens_pedido.id_pizza = pizza.id_pizza "
                        "group by itens_pedido.id_pizza ORDER BY pizza.nome_pizza")
    rows = data.cursor.fetchall()
    pizza = []
    vendidos = []
    for row in rows:
        pizza.append(row[0])
        vendidos.append(row[1])

    vendidosDIC = {'Pizza:': pizza,
                   'Vendas': vendidos}

    vendidosDF = pd.DataFrame(vendidosDIC)

    print(vendidosDF)

    getChar = input("Aperte Enter para continuar...")