from util import *
from models import Conta
from crud_db import *

def consultar_contas():
    contas = consultar_contas_db()
    print()
    for conta in contas:
        print(conta)
    print()

def consultar_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if (not conta): 
        print("Erro: conta não existe")
        return
    print(conta)

def incluir_conta():
    nome = entrar_nome()
    saldo = entrar_saldo()
    incluir_conta_db(nome, saldo)

def excluir_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não existe")
        return
    excluir_conta_db(id)

def alterar_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não existe")
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if (oper == "C"):
        conta.creditar(valor)
    else:
        conta.debitar(valor)
    alterar_conta_db(conta) #está passando o objeto conta que foi criado com os dados consultados do banco via sql
