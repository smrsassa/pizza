import database.db as data

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
    print("| [3] Produtos")
    print("| [4] Sair")
    print("|" + "==" * 19 + "|")
    index_opc = input("Qual a opc: ")
    index_opc = int(index_opc)
    while True:
        if index_opc in [1, 2, 3, 4]:
            return index_opc
        else:
            index_opc = input("Opc invalida! Digite novamente: ")
            int(index_opc)

#====== Atendimento =================================================
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
    in_user(tel_fixo,tel_cel,nome_cli,endereco,nr_end,complemento,bairro,cidade,uf,cep)

def pedido_index(id_user):
    pizza = []
    tam = []
    string1 = "itens_pedido.id_ped = pedido.id_ped and pedido.id_user = {} and ".format(id_user)
    string2 = "itens_pedido.id_pizza = pizza.id_pizza ORDER BY item DESC LIMIT 3"
    string = string1 + string2
    data.cursor.execute("SELECT pizza.nome_pizza from itens_pedido, pedido, user, pizza WHERE "+string)
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
        tamanho = input("| [1]Normal\n[2]Media\n[3]Grande\n[4]Gigante\n Qual o tamanho da pizza desejada: ")
        tam.append(tamanho)
        cont = int(input("[1]Sim\n[2]Não\nMais algum pedido?"))
        if cont == 2:
            break

    import func.insert_sql as insert
    insert.fechando_pedido(pizza, tam, id_user)
#====== Pedidos =================================================





#====== Produtos =================================================