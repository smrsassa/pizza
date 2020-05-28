"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
Descrição..: Esse arquivo tem o objetivo de unir todas as funcionalidades da aplicação
a partir de funções
"""

import include as inc

inc.msg.cabecalho()

#Mds python não tem switch?????
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
            inc.msg.inserir_pizza()
        elif opc == 2:
            inc.msg.editar_pizza()
        elif opc == 3:
            inc.msg.inativar_pizza()
        elif opc == 4:
            inc.selSql.vendas()
        else:
            pass

    else:

        exit()