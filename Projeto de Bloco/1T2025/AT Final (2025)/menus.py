from crud_usuario import *
from crud_livro import *
from crud_biblioteca import *
from crud_emprestimos import *
from crud_devolucoes import *
import os

def chamada_inicial():

    print(f"{'=' * 18} SISTEMA DE GERENCIAMENTO DE BIBLIOTECA {'=' * 18}".center(os.get_terminal_size().columns))
    print(f"{'=' * 10} Projeto de Bloco - Fundamento de Dados - Projeto Final {'=' * 10}".center(os.get_terminal_size().columns))
    print(f"{'=' * 16} Feito por: André Loureiro Montini Ferreira {'=' * 16}".center(os.get_terminal_size().columns))
    print("\nInicializando banco de dados...")



def mostrar_menu_principal():
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Livros")
        print("3. Realizar um Empréstimo")
        print("4. Realizar uma Devolução")
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
            print("Saindo do sistema...\n")
            print(f"{'=' * 23} Obrigado por usar o sistema! {'=' * 23}".center(os.get_terminal_size().columns))
            print(f"{'=' * 10} Projeto de Bloco - Fundamento de Dados - Projeto Final {'=' * 10}".center(os.get_terminal_size().columns))
            print(f"{'=' * 16} Feito por: André Loureiro Montini Ferreira {'=' * 16}".center(os.get_terminal_size().columns))

            break
        else:
            print("Opção inválida!")



def mostrar_menu_usuarios():
    while True:
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário")
        print("4. Editar usuário")
        print("5. Excluir usuário")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            editar_usuario()
        elif opcao == '5':
            excluir_usuario()
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
        print("5. Quantidade de empréstimos ativos por usuário")
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
        elif opcao == '5':
            quantidade_emprestimos_ativos_por_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")
