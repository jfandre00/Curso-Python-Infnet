def menu(): 
    '''
    Função que exibe o menu de opções para o usuário

    return: None
    '''
    while True:
        print(f"{'='*30} Menu de Opções {'='*30}".center(100))
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Ordenar produtos por quantidade")
        print("4 - Buscar produto")
        print("5 - Remover produto com base no código")
        print("6 - Consulta de produtos esgotados")
        print("7 - Consulta de produtos com baixa quantidade")
        print("8 - Atualizar estoque")
        print("9 - Atualizar preço de venda\n")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print("Cadastro de produtos".center(100))
            case "2":
                print("Listagem de produtos".center(100))
            case "3":
                print("Ordenar produtos por quantidade".center(100))
            case "4":
                print("Buscar produto".center(100))
            case "5":
                print("Remover produto".center(100))
            case "6":
                print("Consulta de produtos esgotados".center(100))
            case "7":
                print("Consulta de produtos com baixa quantidade".center(100))
            case "8":
                print("Atualizar estoque".center(100))
            case "9":
                print("Atualizar preço de venda".center(100))
            case "0":
                print(f"{'='*30} Saindo... {'='*30}".center(100))
                break
            case _:
                print("Opção inválida")    


if __name__ == "__main__":
    menu()
