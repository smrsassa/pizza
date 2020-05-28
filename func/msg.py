"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
Descrição..: Esse arquivo contem funções que exibem mensages e menus para o usuario
"""
import database.db as data
import include as inc


def cls_clear():
    from os import system, name
    if name == "nt":
        system("cls")
    else:
        system("clear")


def cabecalho():
    print("|" + "==" * 19 + "|")
    print("|      Bem Vindo ao Sistema da:        |")
    print("| MASTER-PIZZA’S ENTREGAS RAPIDAS LTDA |")
    print("|" + "==" * 19 + "|")


def index_menu():
    print("|" + "==" * 19 + "|")
    print("| [1] Atendimento")
    print("| [2] Pedidos")
    print("| [3] Produtos / Clientes")
    print("| [4] Sair")
    print("|" + "==" * 19 + "|")
    index_opc = int(input("| Qual a opc: "))
    while True:
        if index_opc in [1, 2, 3, 4]:
            return index_opc
        else:
            index_opc = int(input("Opc invalida! Digite novamente: "))


# ====== Atendimento =================================================
def atendimento_index():
    cls_clear()
    print("|" + "==" * 19 + "|")
    tel = str(input("Digite o numero do telefone: "))
    return tel


def cadastra_cliente():
    print("|" + "==" * 19 + "|")
    print("| Cadastro de cliente:                 |")
    tel_fixo = input("Telefone fixo: ")
    tel_cel = input("Telefone celular: ")
    nome_cli = input("Nome: ")
    endereco = input("Endereço: ")
    nr_end = input("Numero do endereço: ")
    complemento = input("Complemento: ")
    bairro = input("bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    cep = input("CEP: ")

    from func.insert_sql import in_user
    in_user(tel_fixo, tel_cel, nome_cli, endereco, nr_end, complemento, bairro, cidade, uf, cep)


def pedido_index(id_user):
    pizza = []
    tam = []

    string1 = "itens_pedido.id_ped = pedido.id_ped and pedido.id_user = {} and ".format(id_user)
    string2 = "itens_pedido.id_pizza = pizza.id_pizza ORDER BY item DESC LIMIT 3"
    string = string1 + string2
    data.cursor.execute("SELECT pizza.nome_pizza from itens_pedido, pedido, user, pizza WHERE " + string)
    pedido = data.cursor.fetchall()

    if pedido:
        print("| Ultimos pedidos do cliente: ")
        for item in pedido:
            print("| - {}".format(item[0]))
    else:
        print("| Esse cliente ainda não possui pedidos..")

    while True:
        idPizza = input("| Qual o ID da pizza desejada: ")
        pizza.append(idPizza)
        tamanho = input("| [1]Normal\n| [2]Media\n| [3]Grande\n| [4]Gigante\n| Qual o tamanho da pizza desejada: ")
        tam.append(tamanho)
        cont = int(input("| [1]Sim\n| [2]Não\n| Mais algum pedido?"))
        if cont == 2:
            break

    import func.insert_sql as insert
    insert.fechando_pedido(pizza, tam, id_user)


# ====== Pedidos =================================================

def pedido():
    print("|" + "==" * 19 + "|")
    print("| [1] Pedidos em aberto:")
    print("| [2] Ultimos Pedidos: ")
    print("| [3] Voltar")
    print("|" + "==" * 19 + "|")
    index_opc = int(input("Qual a opc: "))
    while True:
        if index_opc in [1, 2, 3]:
            return index_opc
        else:
            index_opc = int(input("Opc invalida! Digite novamente: "))


def data_pedido():
    from datetime import date
    ano_atual = date.today()
    ano_atual = ano_atual.year

    print("| Digite a data para ver os pedidos que teve naquele dia:")
    dia = int(input("Dia: "))
    while True:
        if dia > 31 or dia < 1:
            dia = int(input("Dia invalido digite novamente: "))
        else:
            dia = str(dia)
            break

    mes = int(input("Mes: "))
    while True:
        if mes > 12 or mes < 1:
            mes = int(input("Mes invalido digite novamente: "))
        else:
            mes = str(mes)
            if len(mes) == 1:
                mes = "0" + mes
            break
    ano = int(input("Ano: "))
    while True:
        if ano > ano_atual:
            ano = int(input("Ano invalido digite novamente: "))
        else:
            ano = str(ano)
            break

    return (ano + "-" + mes + "-" + dia)


# ====== Produtos =================================================

def produto():
    print("|" + "==" * 19 + "|")
    print("| [1] Inserir pizza")
    print("| [2] Editar pizza")
    print("| [3] Inativar pizza")
    print("| [4] Editar clientes")
    print("| [5] Vendas")
    print("| [6] Voltar")
    print("|" + "==" * 19 + "|")
    index_opc = int(input("Qual a opc: "))
    while True:
        if index_opc in [1, 2, 3, 4, 5]:
            return index_opc
        else:
            index_opc = int(input("Opc invalida! Digite novamente: "))


def inserir_pizza():
    nome_pizza = input("| Nome da nova pizza: ")
    ingredientes = input("| Ingredientes da nova pizza: ")
    custo = input("| Preço: ")

    inc.inSql.in_pizza(nome_pizza, ingredientes, custo)

def editar_pizza():
    id_pizza = input("| Id da pizza que deseja editar: ")
    nome_pizza = input("| Nome da nova pizza: ")
    ingredientes = input("| Ingredientes da nova pizza: ")
    custo = input("| Preço: ")

    inc.upSql.up_pizza(id_pizza, nome_pizza, ingredientes, custo)


def inativar_pizza():
    id_pizza = input("| Id da pizza que deseja INATIVAR: ")

    inc.upSql.invalidar_pizza(id_pizza)


def editar_usuario():
    id_cliente = input("| Id do cliente que deseja editar: ")
    tel_fixo = input("| Telefone fixo: ")
    tel_cel = input("| Telefone celular: ")
    nome_cli = input("| Nome: ")
    endereco = input("| Endereço: ")
    nr_end = input("| Numero da casa: ")
    complemento = input("| Complemento: ")
    bairro = input("| Bairro: ")
    cidade = input("| Cidade: ")
    uf = input("| UF: ")
    cep = input("| CEP: ")

    inc.upSql.up_usuario(
        id_cliente, tel_fixo, tel_cel, nome_cli, endereco, nr_end, complemento, bairro, cidade, uf, cep
    )


