from util import *

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
        print(conta[0], conta[1], conta[2])
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
    conta = [id, nome, saldo]
    contas.append(conta)

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
        conta[2] += valor
    else:
        conta[2] -= valor

