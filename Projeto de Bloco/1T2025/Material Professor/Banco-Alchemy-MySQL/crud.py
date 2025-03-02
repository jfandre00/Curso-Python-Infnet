from crud_db import *
from util import *

def consultar_contas():
    contas = consultar_contas_db()
    if (not contas):
        print("Não há contas no banco")
        return
    print("\nContas no banco")
    for conta in contas:
        print(conta)
    print()

def consultar_conta():
    id = entrar_inteiro()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: Conta não existe")
        return
    print()
    print(conta)

def incluir_conta():
    nome = input("Digite o nome do cliente: ")
    saldo = float(input("Digite o saldo do cliente: "))
    conta = Conta(None, nome, saldo) #poderia ser None ou 0
    incluir_conta_db(conta)

def excluir_conta():
    id = entrar_inteiro()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: Conta não existe")
        return
    excluir_conta_db(conta)

def alterar_conta():
    id = entrar_inteiro()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: Conta não existe")
        return
    conta.creditar(float(input("Digite o valor a ser creditado: ")))
    alterar_conta_db(conta)