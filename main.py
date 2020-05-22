"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
"""

import include as inc

inc.msg.cabecalho()
index_opc = inc.msg.index_menu()

#Mds em python não tem switch?????
if index_opc == 1:

    tel = inc.msg.atendimento_index()

    existe = inc.selSql.procura_cliente(tel)
    if existe:
        inc.msg.pedido_index(existe)
    else:
        inc.msg.cadastra_cliente()


elif index_opc == 2:

    print("2")

elif index_opc == 3:

    print("3")

else:

    exit()