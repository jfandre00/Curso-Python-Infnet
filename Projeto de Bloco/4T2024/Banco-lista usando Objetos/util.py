def entrar_id():
    id = int(input('Entre com o número da conta: '))
    return id


def entrar_nome():
    nome = input('Entre com o nome do cliente: ')
    return nome


def entrar_saldo():
    saldo = float(input('Entre com o saldo da conta: '))
    return saldo

def pesquisar_conta(contas, id):
    conta_pesquisada = []
    for conta in contas:
        if id == conta.id:
            conta_pesquisada = conta
            break
    return conta_pesquisada
    #Se não encontrar a conta, retorna uma lista vazia
    #Se encontrar a conta, retorna a lista com os dados da conta existente


def pesquisar_conta_2(contas, id):
    achou = False
    for conta in contas:
        if id == conta.id:
            achou = True
            break
    return achou

def entrar_operacao():
    while True:
        oper = input('[C]rédito ou [D]ébito: ').upper()
        if oper not in ("C", "D"):
            print('Erro: Operação inválida')
        else:
            break
    return oper


def entrar_valor():
    while True:
        valor = float(input('Entre com o valor: '))
        if valor <= 0:
            print('Erro: Valor inválido')
        else:
            break
    return valor