from crud_usuario import *
from crud_livro import *
from crud_biblioteca import *

def mostrar_menu_usuarios():
    while True:
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")


def mostrar_menu_livros():
    while True:
        print("\n=== GERENCIAR LIVROS ===")
        print("1. Listar todos os livros")
        print("2. Buscar livro por título")
        print("3. Buscar livro por autor")
        print("4. Ver disponibilidade")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            buscar_livro_titulo()
        elif opcao == '3':
            buscar_livro_autor()
        elif opcao == '4':
            ver_disponibilidade()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")


def mostrar_menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("1. Empréstimos ativos")
        print("2. Histórico de empréstimos")
        print("3. Livros mais emprestados")
        print("4. Usuários com mais empréstimos")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            relatorio_emprestimos_ativos()
        elif opcao == '2':
            relatorio_historico_emprestimos()
        elif opcao == '3':
            relatorio_livros_mais_emprestados()
        elif opcao == '4':
            relatorio_usuarios_mais_emprestimos()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")
