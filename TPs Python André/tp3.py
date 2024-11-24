#Menu Principal
def menu_principal():
    '''
    Função que exibe o menu principal do TP3 e chama a função correspondente ao exercício escolhido pelo usuário.

    Returns:
        None
    '''
    while True:
        print("\nTP3 André Loureiro Montini Ferreira:")
        print("Escolha uma opção entre 1 a 16 para ver o exercício correspondente ou 0 para Sair:")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            exercicio1()
        elif opcao == '2':
            exercicio2()
        elif opcao == '3':
            exercicio3()
        elif opcao == '4':
            exercicio4()
        elif opcao == '5':
            exercicio5()
        elif opcao == '6':
            exercicio6()
        elif opcao == '7':
            exercicio7()
        elif opcao == '8':
            exercicio8()
        elif opcao == '9':
            exercicio9()
        elif opcao == '10':
            exercicio10()
        elif opcao == '11':
            exercicio11()
        elif opcao == '12':
            exercicio12()
        elif opcao == '13':
            exercicio13()
        elif opcao == '14':
            exercicio14()
        elif opcao == '15':
            exercicio15()
        elif opcao == '16':
            exercicio16()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#Exercício 01
def exercicio1():
    '''
    Lê uma lista de números inteiros separados por espaço e imprime a lista dos quadrados dos números lidos.
    
    Returns: 
        None
    '''
    lista_numeros = list(map(int, input("Entre com os números separados por espaço: ").split()))
    quadrados = [x**2 for x in lista_numeros]
    print(quadrados)

#Exercício 02
def exercicio2():
    '''
    Lê uma lista de números inteiros separados por espaço e imprime a lista dos números lidos que são maiores que 10.

    Returns: 
        None
    '''
    lista_numeros = list(map(int, input("Entre com os números separados por espaço: ").split()))
    retorno = [x if x > 10 else 0 for x in lista_numeros]
    print(retorno)

#Exercício 03
def exercicio3():
    '''
    Conta o número de palavras em cada frase de um texto predefinido e imprime os resultados.

    Returns: 
        None
    '''
    frases = 'Hoje o dia estava ensolarado. Amanhã deve fazer sol também. Ontem e anteontem estava chuvoso ou nublado.'
    lista_frases = frases.strip('.').split('.') #remove o ponto final e divide as frases

    numero_palavras_frase = [len(frase.split()) for frase in lista_frases] #conta o número de palavras em cada frase

    print(numero_palavras_frase)

#Exercício 04
def exercicio4():
    '''
    Conta o número de vogais em cada frase de um texto predefinido e imprime os resultados.

    Returns: 
        None
    '''
    frases = 'Hoje vai ter futebol na TV. Essa semana tem jogo do Corinthians. O time do Palmeiras usa a cor verde no uniforme. O Santos foi o primeiro time brasileiro a vencer a Libertadores.'

    #vogais = ['a', 'e', 'i', 'o', 'u'] No fim nem usei essa lista, coloquei direto na list comprehension, fui refatorando o código.

    lista_frases = frases.lower().strip('.').split('.')

    #vogais_frase = [[letra for letra in frase if letra in 'aeiou'] for frase in lista_frases]

    #Resolvi dessa forma pois foi pedido para uma linha de código, mas acho que a legibilidade do código fica prejudicada.

    quantidade_vogais_frase = [len(frase) for frase in [[letra for letra in frase if letra in 'aeiou'] for frase in lista_frases]] #List comprehension aninhada

    print(quantidade_vogais_frase)

#Exercício 05 (01)
def exercicio5():
    '''
    Filtra e imprime um dicionário com pessoas maiores de idade a partir de um dicionário de idades predefinido.

    Returns: 
        None
    '''
    dicionario_idades = {
        'João': 15,
        'Maria': 30,
        'José': 10,
        'Ana': 25,
        'Pedro': 30,
        'Elisa': 12,
        'Carlos': 35,
        'Lucas': 23,
        'Luisa': 18,
        'Mariana': 26,
        'Fernando': 17,
        'Cristina': 24,
        'Ricardo': 30
    }

    maiores_idade = {nome: idade for nome, idade in dicionario_idades.items() if idade >= 18}

    print(maiores_idade)

#Exercício 06 (02)
def exercicio6():

    def filtro_palavras(frase, palavras_indesejadas):
        '''
        Remove palavras indesejadas de uma frase.

        Args:
            frase (str): Frase de entrada.
            palavras_indesejadas (list): Lista de palavras a serem removidas.

        Returns:
            str: Frase filtrada sem as palavras indesejadas.
        '''
        palavras = frase.split()
        frase_filtrada = [palavra for palavra in palavras if palavra.lower() not in palavras_indesejadas]
        return (' '.join(frase_filtrada))

    palavras_indesejadas = ['briga', 'guerra', 'roubo', 'assalto']
    frase = 'A briga de ontem foi feia. O time de futebol está em guerra. O roubo ocorreu na avenida. O assalto foi a mão armada.'

    nova_frase = filtro_palavras(frase, palavras_indesejadas)
    print(nova_frase)

#Exercício 07 (03)
def exercicio7():

    def alternador_maisculas_minusculas(frase):
        '''
        Função que recebe uma frase e retorna a frase com as letras alternando entre maiúsculas e minúsculas.

        Args:
            frase (str): A frase de entrada a ser modificada.

        Returns:
            str: A frase com letras alternando entre maiúsculas e minúsculas.
        '''
        nova_frase = ''
        for i, letra in enumerate(frase):
            if i % 2 == 0:
                nova_frase += letra.upper()
            else:
                nova_frase += letra.lower()
        return nova_frase

    entrada = 'desenvolvendo habilidades'
    print(alternador_maisculas_minusculas(entrada.strip().lower()))

#Exercício 08 (04)
def exercicio8():
    def contador_elementos_unicos(listas):
        '''
        Função que recebe uma lista de listas e retorna uma lista com os elementos únicos presentes nas listas.

        Args:
            listas (list): Uma lista contendo várias listas de elementos.

        Returns:
            list: Uma lista com elementos únicos presentes nas listas de entrada, ordenada.
        '''
        output = []
        for lista in listas:
            for numero in lista:
                if numero not in output:
                    output.append(numero)
        output.sort()
        return output

    listas = [[9,2,4,6], [4, 7, 5, 1, 6], [2, 7, 1, 2, 6], [3, 7, 8]]
    print(contador_elementos_unicos(listas))

#Exercício 09 (05)
def exercicio9():
    def intercalador_de_listas(maior_lista, menor_lista, tamanho_lista=0):
        '''
        Função que recebe duas listas e retorna uma string com os elementos intercalados.

        Args:
            maior_lista (list): A lista maior de elementos.
            menor_lista (list): A lista menor de elementos.
            tamanho_lista (int, opcional): O comprimento da lista maior, se necessário. Default é 0.

        Returns:
            str: Uma string contendo os elementos das listas intercalados.
        '''
        string = ''
        for i in range(len(menor_lista)):
            string += maior_lista[i] + ' ' + menor_lista[i] + ' '
        if tamanho_lista:
            for i in range(len(menor_lista), tamanho_lista):
                string += maior_lista[i] + ' '
        return string


    lista1 = ['casa', 'carro', 'moto', 'bicicleta', 'caminhão']
    lista2 = ['banana', 'maçã', 'pera', 'uva', 'abacaxi', 'manga', 'melancia']

    if len(lista1) > len(lista2):
        string = intercalador_de_listas(lista1, lista2, len(lista1))
    elif len(lista1) < len(lista2):
        string = intercalador_de_listas(lista2, lista1, len(lista2))
    else:
        string = intercalador_de_listas(lista1, lista2)

    print(string)

#Exercício 10 (06)
def exercicio10():

    def separador_palavras(lista_palavras, COMPRIMENTO_CORTE):
        '''
        Função que recebe uma lista de palavras e um comprimento de corte e retorna uma lista com duas listas,
        uma com as palavras maiores que o comprimento de corte e outra com as palavras menores.

        Args:
            lista_palavras (list): Lista de palavras a serem separadas.
            COMPRIMENTO_CORTE (int): O comprimento de corte para separar as palavras.

        Returns:
            list: Lista contendo duas sublistas, uma com as palavras maiores e outra com as menores.
        '''
        maiores_palavras = []
        menores_palavras = []
        retorno = []
        for palavra in lista_palavras:
            if len(palavra) > COMPRIMENTO_CORTE:
                maiores_palavras.append(palavra)
            else:
                menores_palavras.append(palavra)
        retorno.append(maiores_palavras)
        retorno.append(menores_palavras)
        return retorno
    
    lista_palavras = ['casa', 'carro', 'moto', 'bicicleta', 'caminhão', 'banana', 'maçã', 'pera', 'uva', 'abacaxi', 'manga', 'melancia']

    COMPRIMENTO_CORTE = 4

    retorno = separador_palavras(lista_palavras, COMPRIMENTO_CORTE)
    print(retorno)

#Exercício 11 (07)
def exercicio11():

    def inserir_palavra(lista_palavras, nova_palavra):
        #Eu entendi pelo enunciado que devemos perguntar ao usuário a posição para inserir a palavra, mas se a lista tiver menos de 3 elementos, a palavra é inserida no final da lista. Então primeiro fiz a verificação do tamanho da lista e depois, se necessário, pergunto a posição para inserir a palavra.
        '''
        Função que recebe uma lista de palavras e uma nova palavra e insere a nova palavra na lista,
        dependendo do tamanho da lista. Se a lista tiver menos de 3 elementos, a palavra é adicionada no final.

        Args:
            lista_palavras (list): Lista de palavras existente.
            nova_palavra (str): A nova palavra a ser inserida.

        Returns:
            list: A lista com a nova palavra inserida na posição correta.
        '''
        TAMANHO_MINIMO = 3
        if len(lista_palavras) < TAMANHO_MINIMO:
            lista_palavras.append(nova_palavra)
        else:
            posicao_inserir = int(input("Digite a posição para inserir a palavra: "))
            lista_palavras.insert(posicao_inserir, nova_palavra)
        return lista_palavras

    lista_palavras = ['casa', 'carro', 'moto', 'bicicleta', 'caminhão', 'banana', 'maçã', 'pera', 'uva', 'abacaxi', 'manga', 'melancia']
    nova_palavra = 'laranja'

    print(inserir_palavra(lista_palavras, nova_palavra))

#Exercício 12 (08)
def exercicio12():

    def combinar_listas(lista1, lista2):
        '''
        Combina duas listas em uma única lista.

        Args:
            lista1 (list): A primeira lista a ser combinada.
            lista2 (list): A segunda lista a ser combinada.

        Returns:
            list: Uma lista combinada contendo os elementos de lista1 seguidos pelos de lista2.
        '''
        lista1.extend(lista2)
        return lista1

    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print(combinar_listas(lista1, lista2))

#Exercício 13 (09)
def exercicio13():
    def remover_duplicatas(lista):
        '''
        Remove elementos duplicados de uma lista.

        Args:
            lista (list): A lista com possíveis duplicatas.

        Returns:
            list: Uma nova lista contendo os elementos únicos da lista original.
        '''
        lista_nova = []
        for palavra in lista:
            if palavra in lista_nova:
                continue
            else:
                lista_nova.append(palavra)
        print(lista_nova)

    lista = ['carro', 'banana', 'maça', 'carro', 'uva', 'uva', 'moto', 'uva']

    remover_duplicatas(lista)

#Exercício 14 (10)
def exercicio14():
    def gerenciar_compras(lista_de_compras):
        '''
        Gerencia a lista de compras, permitindo que o usuário remova itens.

        Args:
            lista_de_compras (list): A lista de compras que será gerenciada.

        Returns:
            None
        '''
        
        while True:
            if len(lista_de_compras) == 0:
                    print("Saindo...")
                    break
            resposta = input("Deseja remover o último item da lista de compras? (s/n): ")
            if resposta == 's':
                lista_de_compras.pop()
                print(lista_de_compras if len(lista_de_compras) > 0 else "Lista de compras vazia.")
            else:
                break
            
    lista_de_compras = ['banana', 'maçã', 'pera', 'uva', 'abacaxi', 'manga', 'melancia']
    print(lista_de_compras)
    gerenciar_compras(lista_de_compras)

#Exercício 15 (11)
def exercicio15():
    #Nesse exercício adicionei um tratamento de erro para os índices digitados pelo usuário. Se o índice inicial for maior que o final, se forem negativos ou se o índice final for maior ou igual ao tamanho da frase, o programa exibe uma mensagem de erro e encerra.
    def manipular_string(frase):
        '''
        Manipula uma string, extraindo um trecho baseado em índices fornecidos pelo usuário.

        Args:
            frase (str): A string de onde o trecho será extraído.

        Returns:
            None
        '''

        print(f'Frase original: {frase}')
    
        entrada = input("Digite o primeiro índice que deseja extrair e o último (separados por espaço): ").split()
    
        if len(entrada) != 2:
            print("Você deve digitar dois números inteiros separados por espaço. Saindo...")
            return
    
        try:
            inicio, fim = map(int, entrada)    
            if inicio > fim:
                print("O índice inicial não pode ser maior que o final. Saindo...")
                return
            elif inicio < 0 or fim < 0:
                print("Os índices não podem ser negativos. Saindo...")
                return
            elif fim >= len(frase) or inicio >= len(frase):
                print("Nenhum índice pode ser maior ou igual ao tamanho da frase. Saindo...")
                return
         
            print(f'Frase extraída: {frase[inicio:fim + 1]}')
        except ValueError:
            print("Digite apenas números inteiros. Saindo...")

    manipular_string('Python é incrível!')

#Exercício 16 (12)
def exercicio16():
    def imprimir_lista_compras(lista_compras):
        '''
        Imprime a lista de compras de forma legível.

        Args:
            lista_compras (list): A lista de compras a ser impressa.

        Returns:
            None
        '''

        if len(lista_compras) == 0 or all(item is None for item in lista_compras):
            print("Lista de compras vazia.")
        else:
            print("Lista de compras:")
            for i, item in enumerate(lista_compras):
                if item is not None:
                    print(f"{i}: {item}")

    def remover_item(lista_compras, comando):
        '''
        Remove um item da lista de compras baseado no índice ou no nome do produto.

        Args:
            lista_compras (list): A lista de compras a ser modificada.
            comando (str): O comando para remover um item ('remover [índice ou nome]').

        Returns:
            None
        '''

        try:
            _, argumento = comando.split(" ", 1)
            if argumento.isdigit():  # Remover por índice
                indice = int(argumento)
                if 0 <= indice < len(lista_compras) and lista_compras[indice] is not None:
                    removido = lista_compras.pop(indice)
                    print(f"Item removido: {removido}")
                else:
                    print("Índice inválido.")
            else:  # Remover por nome
                if argumento in lista_compras:
                    lista_compras.remove(argumento)
                    print(f"Item removido: {argumento}")
                else:
                    print("Produto não encontrado na lista.")
        except ValueError:
            print("Comando inválido. Use: 'remover [nome ou índice]'.")

    def adicionar_item(lista_compras, comando):
        '''
        Adiciona um item na lista de compras em um índice especificado.

        Args:
            lista_compras (list): A lista de compras a ser modificada.
            comando (str): O comando para adicionar um item ('adicionar [índice] [nome]').

        Returns:
            None
        '''

        try:
            _, indice, nome = comando.split(" ", 2)
            indice = int(indice)
            if indice < 0:
                print("Índice inválido. Deve ser um valor não negativo.")
            else:
                # Expandir a lista se o índice for maior que o tamanho atual
                while len(lista_compras) <= indice:
                    lista_compras.append(None)
                lista_compras[indice] = nome
                print(f"Item adicionado: {nome} na posição {indice}")
        except ValueError:
            print("Comando inválido. Use: 'adicionar [índice] [nome]'.")

    def gerenciar_lista_compras(lista_compras):
        #Não sei se o enunciado tinha algum erro, mas eu entendi que para 'remover' um item da lista de compras, o usuário precisa digitar o índice 'OU' o nome do produto. Para 'adicionar' um item, o usuário deveria digitar o índice 'E' o nome do produto. Essa foi a forma que prossegui.
        #Eu identifiquei um 'problema' caso o usuário digitasse um índice acima do tamanho da lista ao adicionar um item, então eu adicionei um loop de None para expandir a lista até o índice desejado. Isso não foi pedido, mas eu achei interessante fazer pois eu imagino que o usuário não tem um conhecimento prévio do tamanho da lista.	

        #Como esse é um exercício maior, resolvi refatorar o código para ficar mais organizado.
        '''
        Função principal para gerenciar a lista de compras, permitindo adicionar e remover itens.

        Args:
            lista_compras (list): A lista de compras a ser gerida.

        Returns:
            None
        '''

        while True:
            imprimir_lista_compras(lista_compras)
            comando = input("Digite uma operação ('fim', 'remover [nome ou índice]', 'adicionar [índice] [nome]'): ").strip()
            
            if comando.lower() == "fim":
                break
            elif comando.lower().startswith("remover"):
                remover_item(lista_compras, comando)
            elif comando.lower().startswith("adicionar"):
                adicionar_item(lista_compras, comando)
            else:
                print("Comando não reconhecido.")
        
        print("\nLista final:")
        imprimir_lista_compras(lista_compras)

    lista = []
    gerenciar_lista_compras(lista)

#Inciando o TP3
menu_principal()

