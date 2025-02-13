# CRUD de contas bancárias com id da conta, nome do cliente e saldo

'''C: Create - criar uma conta nova em uma lista
   R: Read - ler da lista ou do banco de dados
   U: Update - atualizar a lista ou o banco de dados
   D: Delete - deletar da lista ou do banco de dados
'''

from crud import *
from menu import *

contas = [
# [id (posição 0), nome (posição 1), saldo (posição 2)]
[1, 'André', 100], 
[2, 'Bruno', 200], 
[3, 'Eloisa', 300], 
[4, 'Murilo', 400]
]

opcao = entrar_opcao()
while (opcao != 0):
    match opcao:
        case 1:
            incluir_conta(contas)
        case 2:
            alterar_conta(contas)
        case 3:
            excluir_conta(contas)
        case 4:
            consultar_contas(contas)
        case 5:
            consultar_conta(contas)
        case _: #default
            print("Opção inválida!")

    opcao = entrar_opcao()




