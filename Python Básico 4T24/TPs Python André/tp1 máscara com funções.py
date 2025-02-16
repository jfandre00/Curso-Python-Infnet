# TP1 André Loureiro Montini Ferreira
def menu():
    while True:
        entrada = input("Digite o exercício (1 a 16) ou 0 para sair: ")
        print(f"Valor digitado: '{entrada}'")  # Para depuração

        try:
            exercicio = int(entrada)
            
            if exercicio == 0:
                print("Saindo...")
                break
            elif exercicio == 1:
                exercicio1()
            elif exercicio == 2:
                exercicio2()
            elif exercicio == 3:
                exercicio3()
            elif exercicio == 4:
                exercicio4()
            elif exercicio == 5:
                exercicio5()
            elif exercicio == 6:
                exercicio6()
            elif exercicio == 7:
                exercicio7()
            elif exercicio == 8:
                exercicio8()
            elif exercicio == 9:
                exercicio9()
            elif exercicio == 10:
                exercicio10()
            elif exercicio == 11:
                exercicio11()
            elif exercicio == 12:
                exercicio12()
            elif exercicio == 13:
                exercicio13()
            elif exercicio == 14:
                exercicio14()
            elif exercicio == 15:
                exercicio15()
            elif exercicio == 16:
                exercicio16()
            else:
                print("Opção inválida, tente novamente!")
        except ValueError:
            print("Entrada inválida! Digite um número entre 0 e 16.")

# Exercício 1
def exercicio1():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print(f'A soma dos números é: {n1 + n2}\n'
          f'A subtração dos números é: {n1 - n2}\n'
          f'A multiplicação dos números é: {n1 * n2}\n'
          f'A divisão inteira dos números é: {n1 // n2}')

# Exercícios 2 a 16
def exercicio2():
    print("Executando o exercício 2")
def exercicio3():
    print("Executando o exercício 3")
def exercicio4():
    print("Executando o exercício 4")
def exercicio5():
    print("Executando o exercício 5")
def exercicio6():
    print("Executando o exercício 6")
def exercicio7():
    print("Executando o exercício 7")
def exercicio8():
    print("Executando o exercício 8")
def exercicio9():
    print("Executando o exercício 9")
def exercicio10():
    print("Executando o exercício 10")
def exercicio11():
    print("Executando o exercício 11")
def exercicio12():
    print("Executando o exercício 12")
def exercicio13():
    print("Executando o exercício 13")
def exercicio14():
    print("Executando o exercício 14")
def exercicio15():
    print("Executando o exercício 15")
def exercicio16():
    print("Executando o exercício 16")

menu()
