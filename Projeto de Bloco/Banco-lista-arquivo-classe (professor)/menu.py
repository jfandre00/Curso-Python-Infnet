def exibir_menu():
    print("----Menu----")
    print("[1] - Incluir")
    print("[2] - Alterar")
    print("[3] - Excluir")
    print("[4] - Consultar contas")
    print("[5] - Consultar conta")
    print("[0] - Sair")

def entrar_opcao():
    while (True):
        exibir_menu()
        opcao = int(input("Entre com a opção: "))
        if (opcao not in (0,1,2,3,4,5)):
            print("Erro: opção inválida")
        else:
            break
    return opcao