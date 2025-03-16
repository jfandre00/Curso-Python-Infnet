from exercício3b import criar_banco
from exercícios4_5 import ler_dados
from exercícios6_7 import consultar_banco

def menu():
    while True:
        print("\n")
        print("TP4 - Projeto de Bloco - André L. M. Ferreira")
        print("Digite a opção desejada")
        print("1 - Criar banco de dados usando Python e SQLite")
        print("2 - Ler dados dos arquivos CSV e inserir no banco de dados")
        print("3 - Consultar banco de dados e salvar resultados em arquivos JSON")
        print("4 - Sair")

        opcao = input("Opção: ")
        if opcao == "1":
            criar_banco()
        elif opcao == "2":
            ler_dados()    
        elif opcao == "3":
            consultar_banco()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()
