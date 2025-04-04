from menus import *
from crud_emprestimos import *
from crud_devolucoes import *
from criar_tabelas import *


def mostrar_menu_principal():
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Livros")
        print("3. Empréstimos")
        print("4. Devoluções")
        print("5. Relatórios")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            mostrar_menu_usuarios()
        elif opcao == '2':
            mostrar_menu_livros()
        elif opcao == '3':
            gerenciar_emprestimos()
        elif opcao == '4':
            gerenciar_devolucoes()
        elif opcao == '5':
            mostrar_menu_relatorios()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


print("=== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ===")
print("Inicializando banco de dados...")
criar_tabelas_db()
mostrar_menu_principal()