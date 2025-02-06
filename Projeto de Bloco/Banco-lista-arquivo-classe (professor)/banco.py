# CRUD de contas bancária com id, nome, saldo
from crud import *
from menu import *
from arquivo import *

contas = ler_contas()
opcao = entrar_opcao()
while (opcao != 0):
    match (opcao):
        case 1: incluir_conta(contas)
        case 2: alterar_conta(contas)
        case 3: excluir_conta(contas)
        case 4: consultar_contas(contas)
        case 5: consultar_conta(contas)
        case _: print("Erro: opção inválida")
    opcao = entrar_opcao()
gravar_contas(contas)