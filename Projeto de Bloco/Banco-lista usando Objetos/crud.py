from util import *
from models import Conta

# Tirei tudo que não foi de CRUD e coloquei em um arquivo separado, chamado util, depois fiz a importação
# O programa principal deve refletir somente o CRUD


def consultar_contas(contas):
    ''' 
    # Método tradicional de impressão de listas 
    for i in range(len(contas)):
        for j in range(len(contas[i])):
            print(contas[i][j], end=' ')
        print()
    '''
    for conta in contas:
        print(conta.id, conta.nome, conta.saldo)
    print()

def consultar_conta(contas):
    id = entrar_id()
    conta = pesquisar_conta(contas, id)
    if not conta: # Se não tem conta, se a conta está vazia	
        print('Erro: Conta não existe')
        return
    print(conta)


def incluir_conta(contas):
    id = entrar_id()
    conta_pesquisada = pesquisar_conta(contas, id)
    if conta_pesquisada:
        print('Erro: Conta já existe')
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    contas.append(Conta(id, nome, saldo))

def excluir_conta(contas):
    id = entrar_id()
    conta_pesquisada = pesquisar_conta(contas, id)
    if not conta_pesquisada:
        print('Erro: Conta não existe')
        return
    contas.remove(conta_pesquisada)


def alterar_conta(contas):
    id = entrar_id()
    conta = pesquisar_conta(contas, id)
    if not conta:
        print('Erro: Conta não existe')
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if oper == 'C':
        conta.creditar(valor)
    else:
        conta.debitar(valor)

