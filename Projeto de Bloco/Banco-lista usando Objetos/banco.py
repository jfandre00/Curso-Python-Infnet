# CRUD de contas bancárias com id da conta, nome do cliente e saldo

'''C: Create - criar uma conta nova em uma lista
   R: Read - ler da lista ou do banco de dados
   U: Update - atualizar a lista ou o banco de dados
   D: Delete - deletar da lista ou do banco de dados
'''

from crud import *
from menu import *
from arquivo import *

contas = ler_contas()

for conta in contas:
    print(conta)


opcao = entrar_opcao()
while (opcao != 0):
    match opcao:
        case 1: incluir_conta(contas)
        case 2: alterar_conta(contas)
        case 3: excluir_conta(contas)
        case 4: consultar_contas(contas)
        case 5: consultar_conta(contas)
        case _: print("Opção inválida!")
    opcao = entrar_opcao()

gravar_contas(contas)


