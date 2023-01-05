import pprint
import pymongo


client = pymongo.MongoClient(
    'mongodb+srv://InstituicaoBancaria:diome124@cluster0.vkbazm2.mongodb.net/?retryWrites=true&w=majority')
db = client.Bank
clientes = db.clientes

menu = f'''
    (I)  Incluir Cliente
    (E)  Excluir Cliente
    (EB) Excluir o Banco de Clientes
    (C)  Consulta Clientes
    (S)  Sair
'''


def inserir_cliente():
    cliente = {
        "nome": "MARCIO",
        "cpf": 2222,
        "endereco": "RUA SAID 57",
        "conta_corrente": 1114,
        "agencia": 5555
    }
    return cliente


while True:
    print(menu)
    opcao = input(f'Escolha a opção: ').upper()
    if opcao == 'I':
        cliente = inserir_cliente()
        clientes.insert_one(cliente)
        print('Sucesso, cliente incluido')

    elif opcao == 'E':
        clientes.delete_one({})

    elif opcao == 'S':
        break

    elif opcao == 'EB':
        db.clientes.drop()
        print('O BANCO DE DADOS FOI EXCLUÍDO COMPLETAMENTE, PRESS ENTER')
        input()

    elif opcao == 'C':
        if db.list_collection_names() == []:
            print('NÃO HA CLIENTES CADASTRADOS, PRESS ENTER')
            input()
        else:
            for i in clientes.find():
                print(f"{18 * '.'} C/C {18 * '.'}")
                pprint.pprint(i)
                print(f"{42 * '-'}")

    else:
        print(f'Opção invalida!')
