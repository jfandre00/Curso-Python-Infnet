#TP1 - André Loureiro Montini Ferreira
import random

print("Bem vindo ao TP1 de André Loureiro Montini Ferreira")

while True:
    entrada = input("Digite o número do exercício ([1 a 16] ou 0 para sair): ")
    if entrada == "0":
        print("Saindo...")
        break
    elif entrada == "1":
        print("Exercício 1")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        soma = n1 + n2
        subtracao = n1 - n2
        multiplicacao = n1 * n2
        divisao = n1 / n2
        divisao_inteira = n1 // n2
        print(f"Soma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao} \nDivisão: {divisao} \nDivisão inteira: {divisao_inteira}")
        print("Fim do exercício 1")
        print()
    elif entrada == "2":
        print("Exercício 2")
        minutos = int(input("Digite o número de minutos: "))
        horas = minutos // 60
        minutos_restantes = minutos % 60
        print(f"{minutos} minutos são {horas} horas e {minutos_restantes} minutos")
        minutos_reconvertidos = horas * 60 + minutos_restantes
        print(f"{horas} horas e {minutos_restantes} minutos são {minutos_reconvertidos} minutos")
        print("Fim do exercício 2")
        print()
    elif entrada == "3":
        print("Exercício 3")
        nome1 = input("Digite o primeiro nome: ")
        nome2 = input("Digite o segundo nome: ")
        novo_nome = nome1[:len(nome1)//2] + nome2[len(nome2)//2:]
        #Peguei a primeira metade do primeiro nome e a segunda metade do segundo nome para criar um novo nome
        print(f"O novo nome é {novo_nome}")
        print("Fim do exercício 3")
        print()
    elif entrada == "4":
        print("Exercício 4")
        opcao = input("Escolha a operaçao (adição (1), subtração (2), multiplicação (3) ou divisão(4)): ")
        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida, saindo do exercício 4")
            continue
        n1,n2 = map(int,input("Digite os dois números separados por espaço: ").split())
        if opcao == "1":
            resultado = n1 + n2
            print(f"A soma entre {n1} e {n2} é {resultado}")
        elif opcao == "2":
            resultado = n1 - n2
            print(f"A subtração entre {n1} e {n2} é {resultado}")
        elif opcao == "3":
            resultado = n1 * n2
            print(f"A multiplicação entre {n1} e {n2} é {resultado}")
        elif opcao == "4":
            resultado = n1 / n2
            print(f"A divisão entre {n1} por {n2} é {resultado}")
        print("Fim do exercício 4")
        print()
    elif entrada == "5":
        print("Exercício 5")
        nome = input("Digite o nome: ")
        sobre_nome = input("Digite o sobrenome: ") 
        print(f"Bem vindo ao meu TP1, {nome} {sobre_nome}, espero que goste!")
        print("Fim do exercício 5")
        print()
    elif entrada == "6":
        print("Exercício 6")
        print("Tente adivinhar o número secreto!")
        numeroSecreto = 42
        tentativa = int(input("Digite um número: "))
        if tentativa == numeroSecreto:
            print("Parabéns, o palpite está correto!")
        elif tentativa < numeroSecreto:
            print("O seu palpite está muito baixo")
        else:
            print("O seu palpite está muito alto")
        print("Fim do exercício 6")
        print()
    elif entrada == "7":
        print("Exercício 7")
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros: "))
        imc = peso / (altura**2)
        print(f"O IMC é {imc:.2f}")
        if imc < 18.5:
            print("Abaixo do peso")
        elif imc < 25:
            print("Peso normal")
        else:
            print("Sobrepeso")
        print("Fim do exercício 7")
        print()
    elif entrada == "8":
        print("Exercício 8")
        idade = int(input("Digite a sua idade: "))
        if idade >= 18:
            print("Maior de idade")
        else:
            print("Menor de idade")
        print("Fim do exercício 8")
        print()
    elif entrada == "9":
        print("Exercício 9")
        compra = float(input("Digite o valor da compra: "))
        if compra > 500:
            desconto = 0.25
        elif compra > 200:
            desconto = 0.15
        elif compra > 100:
            desconto = 0.10
        else: 
            desconto = 0
        valor_desconto = compra * desconto
        valor_final = compra - valor_desconto
        print(f"O valor da compra com desconto é R${valor_final:.2f}")
        print("Fim do exercício 9")
        print()
    elif entrada == "10":
        print("Exercício 10")
        personagens = ["Mario", "Luigi", "Peach", "Toad", "Yoshi"]
        acoes = ["pular", "correr", "pegar moedas", "pegar cogumelos", "pegar estrelas"]
        locais = ["no castelo", "no mundo 1-1", "no mundo 1-2", "no mundo 1-3", "no mundo 1-4"]
        personagem = random.choice(personagens)
        acao = random.choice(acoes)
        local = random.choice(locais)
        print(f"{personagem} foi {acao} {local}")
        print("Fim do exercício 10")
        print()
    elif entrada == "11":
        print("Exercício 11")
        dados = int(input("Digite quantos dados deseja lançar:"))
        for i in range(dados):
            print(f"Dado {i+1}: {random.randint(1,6)}")
        print("Fim do exercício 11")
        print()
    elif entrada == "12":
        print("Exercício 12")
        palavra = input("Digite uma palavra: ")
        if len(palavra) < 5:
            print("Palavra curta")
        else:
            print("Palavra longa")
        print("Fim do exercício 12")
        print()
    elif entrada == "13":
        print("Exercício 13")
        palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ").strip().lower().replace(" ","")
        if palavra == palavra[::-1]:
            print("É um palíndromo")
        else:
            print("Não é um palíndromo")
        print("Fim do exercício 13")
        print()
    elif entrada == "14":
        print("Exercício 14")
        votos = [0,0,0]
        opcoes = ["A","B","C"]
        while True:
            voto = input("Digite a opção desejada (A, B ou C) ou 0 para sair: ").upper()
            if voto == "0":
                break
            if voto not in opcoes:
                print("Opção inválida")
                continue
            votos[opcoes.index(voto)] += 1
        for i in range(3):
            print(f"Opção {opcoes[i]}: {votos[i]} votos")
        print("Fim do exercício 14")
        print()
    elif entrada == "15":
        print("Exercício 15")
        def inicio():
            print("Você acorda em uma floresta misteriosa e não se lembra de como chegou lá.")
            print("Ao seu redor, você vê um caminho para a esquerda e outro para a direita.")
            escolha1 = input("Para onde você vai? Digite 'esquerda' ou 'direita': ").lower()
            
            if escolha1 == "esquerda":
                caminho_esquerda()
            elif escolha1 == "direita":
                caminho_direita()
            else:
                print("Escolha inválida. Tente novamente.")
                inicio()

        def caminho_esquerda():
            print("\nVocê escolheu o caminho da esquerda e encontra um lago tranquilo.")
            escolha2 = input("Deseja 'beber' a água ou 'ignorar' o lago e continuar caminhando? ").lower()
            
            if escolha2 == "beber":
                print("\nA água estava envenenada! Você perdeu. Fim do jogo.")
            elif escolha2 == "ignorar":
                print("\nVocê segue em frente e encontra uma cabana. Alguém abre a porta e oferece abrigo.")
                cabana()
            else:
                print("Escolha inválida. Tente novamente.")
                caminho_esquerda()

        def caminho_direita():
            print("\nVocê escolheu o caminho da direita e encontra uma ponte velha.")
            escolha3 = input("Deseja 'atravessar' a ponte ou 'voltar' pelo caminho? ").lower()
            
            if escolha3 == "atravessar":
                print("\nA ponte é frágil e você cai no rio! Fim do jogo.")
            elif escolha3 == "voltar":
                print("\nVocê volta para o ponto inicial.")
                inicio()
            else:
                print("Escolha inválida. Tente novamente.")
                caminho_direita()

        def cabana():
            print("\nNa cabana, você encontra uma pessoa que oferece ajuda para sair da floresta.")
            escolha4 = input("Deseja 'aceitar' a ajuda ou 'recusar' e seguir sozinho? ").lower()
            
            if escolha4 == "aceitar":
                print("\nA pessoa te leva para fora da floresta em segurança. Parabéns, você venceu!")
            elif escolha4 == "recusar":
                print("\nVocê se perde e nunca mais é visto. Fim do jogo.")
            else:
                print("Escolha inválida. Tente novamente.")
                cabana()

        inicio()
        print("Fim do exercício 15")
        print()
    elif entrada == "16":
        print("Exercício 16")
        numero = int(input("Digite um número para verificar se é par ou ímpar: "))
        if numero % 2 == 0:
            print("O número inserido é par")
        else:
            print("O número inserido é ímpar")
        print("Fim do exercício 16")
        print()
    
    else:
        print("Opção inválida, tente novamente")
