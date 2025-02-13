from util import *
from models import Conta

def consultar_contas(contas):
    for conta in contas:
        print(conta)
    print()

def consultar_conta(contas):
    id = entrar_id()
    conta = pesquisar_conta(contas, id)
    if (not conta): #(conta == []):
        print("Erro: conta não existe")
        return
    print(conta)

def incluir_conta(contas):
    id = entrar_id()
    conta_pesquisada = pesquisar_conta(contas, id)
    if (conta_pesquisada):
        print("Erro: conta já existe")
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    contas.append(Conta(id, nome, saldo))

def excluir_conta(contas):
    id = entrar_id()
    conta_pesquisada = pesquisar_conta(contas, id)
    if (not conta_pesquisada):
        print("Erro: conta não existe")
        return
    contas.remove(conta_pesquisada)

def alterar_conta(contas):
    id = entrar_id()
    conta= pesquisar_conta(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if (oper == "C"):
        conta.creditar(valor)
    else:
        conta.debitar(valor)
