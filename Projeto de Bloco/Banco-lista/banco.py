# CRUD de contas bancárias com id da conta, nome do cliente e saldo

'''C: Create - criar uma conta nova em uma lista
   R: Read - ler da lista ou do banco de dados
   U: Update - atualizar a lista ou o banco de dados
   D: Delete - deletar da lista ou do banco de dados
'''

from crud import *


contas = [
# [id (posição 0), nome (posição 1), saldo (posição 2)]
    [1, 'André', 100], 
    [2, 'Bruno', 200], 
    [3, 'Eloisa', 300], 
    [4, 'Murilo', 400]
    ]

consultar_contas(contas)
#incluir_conta(contas)
#excluir_conta(contas)
alterar_conta(contas)
consultar_contas(contas)

#preparar menu 6 opcoes: 4 consultar contas, 1 incluir, 3 excluir, 2 alterar, 5 consultar conta, 0 sair - DE FORMA REFATORADA
