"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
"""

import include as inc

inc.msg.cabecalho()

#Mds em python não tem switch?????
while True:
    #menu principal
    index_opc = inc.msg.index_menu()

    if index_opc == 1:

        tel = inc.msg.atendimento_index()

        existe = inc.selSql.procura_cliente(tel)
        if existe:
            inc.msg.pedido_index(existe)
        else:
            inc.msg.cadastra_cliente()


    elif index_opc == 2:

        opc = inc.msg.pedido()
        if opc == 1:
            inc.selSql.pedidos_aberto()
        elif opc == 2:
            data = inc.msg.data_pedido()
            inc.selSql.ultimos_pedidos(data)
        else:
            pass

    elif index_opc == 3:

        opc = inc.msg.produto()

        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            inc.selSql.vendas()
        else:
            pass

    else:

        exit()