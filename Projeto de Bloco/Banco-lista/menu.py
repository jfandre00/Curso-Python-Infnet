def exibir_menu():
    print("-----Menu-----")
    print("[1] - Incluir conta")
    print("[2] - Alterar conta")
    print("[3] - Excluir conta")
    print("[4] - Consultar contas")
    print("[5] - Consultar conta específica")
    print("[0] - Sair")

def entrar_opcao():
    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))
        if (opcao not in [1, 2, 3, 4, 5, 0]):
            print("Erro: Opção inválida!")
        else:
            break
    return opcao