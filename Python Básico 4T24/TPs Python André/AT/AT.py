#AT de André Loureiro Montini Ferreira
#OBS: Requisito 15 (comentários e docstrings) está espalhado pelo código
#OBS2: Requisito 12 está no tratamentos.py
#OBS3: Gostaria de ter formatado as saídas com cores (por exemplo: print('\033[0;30;41mTestando\033[m')) e utilizado a função clear do os para limpar a tela, mas o JDoodle não rodou direito com um TP que eu tinha feito isso, então deixei para lá.

from tratamentos import *

def criar_estoque(estoque_inicial): #Requisito 2
    '''
    Função que cria o estoque a partir de uma string que está separada por # e ;

    estoque_inicial: str -> string com os produtos do estoque

    return: list -> lista de dicionários com os produtos do estoque
    '''
    estoque = []
    for item in estoque_inicial.split("#"):
        nome, codigo, qtd, preco_custo, preco_venda = item.split(";")
        estoque.append({"nome": nome, "codigo": codigo, "qtd": int(qtd), "preco_custo": float(preco_custo), "preco_venda": float(preco_venda)})
    return estoque

def listar_produtos(estoque): #Requisito 3
    '''
    Função que lista os produtos do estoque

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    print("============= Lista de produtos =============".center(80))
    print()
    for i, produto in enumerate(estoque, 1):
        print(f"{i} - {produto['nome']} - Código: {produto['codigo']} - Qtd: {produto['qtd']} - Preço de custo: R$ {produto['preco_custo']:.2f} - Preço de venda: R$ {produto['preco_venda']:.2f}")
    print("============= Fim da lista =============".center(80))
    print()

def cadastrar_produto(estoque): #Requisito 1
    '''
    Função que cadastra um produto no estoque

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    nome = obter_input_valido("Digite o nome do produto: ", variavel_vazia, "Nome inválido! Tente novamente")
    codigo = obter_input_valido("Digite o código do produto: ", lambda x: variavel_vazia(x) or codigo_existe(x, estoque) or not x.isnumeric(), "Código inválido ou já existe! Tente novamente")
    qtd = obter_input_valido("Digite a quantidade do produto: ", lambda x: variavel_vazia(x) or not x.isnumeric(), "Quantidade inválida! Tente novamente")
    preco_custo = obter_input_valido("Digite o preço de custo do produto: ", lambda x: variavel_vazia(x) or not x.replace(".", "", 1).isnumeric(), "Preço de custo inválido! Tente novamente")
    preco_venda = obter_input_valido("Digite o preço de venda do produto: ", lambda x: variavel_vazia(x) or not x.replace(".", "", 1).isnumeric(), "Preço de venda inválido! Tente novamente")
    #Voltei aqui depois de implementar a função validar_preco_venda para aproveitar a validação
    if not validar_estoque_ou_preco(preco_venda=float(preco_venda), preco_custo=float(preco_custo)):
        print("Comece o cadastro novamente") 
        return
    estoque.append({"nome": nome.strip(), "codigo": codigo.strip(), "qtd": int(qtd), "preco_custo": float(preco_custo), "preco_venda": float(preco_venda)})
    print("Produto cadastrado com sucesso!")

def ordenar_produtos_por_quantidade(): #Requisito 4
    '''
    Função que ordena os produtos por quantidade. O usuário pode escolher exibir em ordem crescente ou decrescente

    return: None
    '''
    if estoque_esta_vazio(estoque):
        print("Não há produtos para ordenar")
        return
    while True:
        pergunta = input("Deseja ordenar em ordem crescente [1] ou decrescente [2]? ")
        if pergunta == "1":
            estoque.sort(key=lambda x: x['qtd'])
            print("Produtos ordenados por quantidade com sucesso!")
            listar_produtos(estoque)
            break
        elif pergunta == "2":
            estoque.sort(key=lambda x: x['qtd'], reverse=True)
            print("Produtos ordenados por quantidade com sucesso!")
            listar_produtos(estoque)
            break
        else:
            print("Opção inválida! Tente novamente")
            continue
            
            

def buscar_produto(escolha, busca): #Requisito 6
    '''
    Função que busca um produto no estoque por descrição ou código

    escolha: str -> escolha do usuário
    busca: str -> código do produto

    return: None
    '''
    if escolha == "1":
        encontrados = [produto for produto in estoque if busca.lower() in produto['nome'].lower()]
        if encontrados:
            for produto in encontrados:
                gerar_print_produto(produto)
        else:
            print("Produto não encontrado")
        return
    elif escolha == "2":
        for produto in estoque:
            if produto['codigo'] == busca:
                gerar_print_produto(produto)
                return
    print("Produto não encontrado")

def remover_produto(estoque): #Requisito 7
    '''
    Função que remove um produto do estoque

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    #Para pegar o código do produto, utilizei a função obter_input_valido com a condição sendo a função lambda para validar se o input é vazio ou não é numérico. Sempre que foi necessário pegar o código do produto, utilizei essa função
    codigo = obter_input_valido("Digite o código do produto: ", lambda x: variavel_vazia(x) or not x.isnumeric(), "Código inválido! Tente novamente")
    #Utilizei a função enumerate para pegar o índice do produto no estoque e o próprio produto
    for i, produto in enumerate(estoque):
        if produto['codigo'] == codigo:
            del estoque[i]
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado")

def consulta_produtos_esgotados(estoque): #Requisito 8
    '''
    Função que consulta os produtos esgotados

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    #Para pegar os produtos esgotados, utilizei uma list comprehension para filtrar os produtos com quantidade igual a 0
    esgotados = [produto for produto in estoque if produto['qtd'] == 0]
    if esgotados:
        print("============= Produtos esgotados =============".center(80))
        for produto in esgotados:
            gerar_print_produto(produto)
        print("============= Fim da lista =============".center(80))
    else:
        print("Não há produtos esgotados")

def produtos_com_baixa_quantidade(estoque, quantidade=10): #Requisito 9
    #Escolhi o valor padrão 10 para a quantidade mínima de produtos com baixa quantidade
    '''
    Função que consulta os produtos com baixa quantidade

    quantidade: int -> quantidade mínima de produtos

    return: None
    '''
    #Para pegar os produtos com baixa quantidade, utilizei a função filter com uma função lambda para filtrar os produtos com quantidade menor que a quantidade mínima
    baixa_quantidade = list(filter(lambda x: x['qtd'] < quantidade, estoque))
    if baixa_quantidade:
        print("============= Produtos com baixa quantidade =============".center(80))
        for produto in baixa_quantidade:
            gerar_print_produto(produto)
        print("============= Fim da lista =============".center(80))
    else:
        print("Não há produtos com baixa quantidade")

def atualizar_estoque(estoque, operacao): #Requisito 10
    '''
    Função que atualiza o estoque

    estoque: list -> lista de dicionários com os produtos do estoque
    operacao: str -> operação a ser realizada

    return: None
    '''
    codigo = obter_input_valido("Digite o código do produto: ", lambda x: variavel_vazia(x) or not x.isnumeric(), "Código inválido! Tente novamente")
    for produto in estoque:
        if produto['codigo'] == codigo:
            qtd = obter_input_valido("Digite a quantidade do produto: ", lambda x: variavel_vazia(x) or not x.isnumeric(), "Quantidade inválida! Tente novamente")
            if operacao == "adicionar":
                produto['qtd'] += int(qtd)
            if operacao == "remover":
                #Chamando a função validar_estoque_ou_preco para validar a atualização do estoque dentro das condições do AT (Requisito 12)
                if not validar_estoque_ou_preco(estoque=estoque, codigo=codigo, numero=int(qtd)):
                    return
                produto['qtd'] -= int(qtd)
            print("Estoque atualizado com sucesso!")
            return
        if produto == estoque[-1]:
            print("Produto não encontrado")

def atualizar_preco_venda(estoque): #Requisito 11
    '''
    Função que atualiza o preço de venda a partir do código do produto após validar se o preço de venda é maior que o preço de custo

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    codigo = obter_input_valido("Digite o código do produto: ", lambda x: variavel_vazia(x) or not x.isnumeric(), "Código inválido! Tente novamente")
    for produto in estoque:
        if produto['codigo'] == codigo:
            #Para pegar o novo preço de venda, utilizei a função obter_input_valido com a condição sendo a função lambda para validar se o input é vazio ou não é numérico
            preco_venda = obter_input_valido("Digite o novo preço de venda do produto: ", lambda x: variavel_vazia(x) or not x.replace(".", "", 1).isnumeric(), "Preço de venda inválido! Tente novamente")
            #Chamando a função validar_estoque_ou_preco para validar o preço de venda dentro das condições do AT (Requisito 12)
            if not validar_estoque_ou_preco(preco_venda=float(preco_venda), preco_custo=produto['preco_custo']):
                return
            produto['preco_venda'] = float(preco_venda)
            print("Preço de venda atualizado com sucesso!")
            return
        #Caso o produto não seja encontrado, exibe a mensagem "Produto não encontrado"
        if produto == estoque[-1]:
            print("Produto não encontrado")

def calcular_valor_total_estoque(estoque): #Requisito 13
    '''
    Função que calcula o valor total do estoque baseado na quantidade e preço de venda de cada produto

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    #Para calcular o valor total do estoque, utilizei a função sum com uma list comprehension para somar o valor total de cada produto
    total = sum(produto['qtd'] * produto['preco_venda'] for produto in estoque)
    print(f"O valor total do estoque é R$ {total:.2f}")

def calcular_lucro_presumido_estoque(estoque): #Requisito 14
    '''
    Função que calcula o lucro presumido do estoque baseado na quantidade, preço de custo e preço de venda de cada produto

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    lucro = sum((produto['preco_venda'] - produto['preco_custo']) * produto['qtd'] for produto in estoque)
    print(f"O lucro presumido do estoque é R$ {lucro:.2f}")
    
def relatorio_geral_estoque(estoque): #Requisito 16
    '''
    Função que exibe um relatório geral do estoque, incluindo a descrição, código, quantidade, custo, preço de venda, e o valor total por item (quantidade * preço). Ao final do relatório, exibe o custo total e o faturamento total do estoque.

    estoque: list -> lista de dicionários com os produtos do estoque

    return: None
    '''
    print("============= Relatório geral do estoque =============".center(80))
    print()
    print("Descrição".ljust(30), "Código".ljust(10), "Quantidade".ljust(10), "Preço de custo".ljust(15), "Preço de venda".ljust(15), "Valor total".ljust(15))
    print()
    for produto in estoque:
        #Para usar os critérios de formatação que foram pedidos no AT, não utilizei a função gerar_print_produto e sim o código abaixo
        print(produto['nome'].ljust(30), produto['codigo'].ljust(10), str(produto['qtd']).ljust(10), f"R$ {produto['preco_custo']:.2f}".ljust(15), f"R$ {produto['preco_venda']:.2f}".ljust(15), f"R$ {produto['qtd'] * produto['preco_venda']:.2f}".ljust(15))
    print()
    custo_total = sum(produto['qtd'] * produto['preco_custo'] for produto in estoque)
    faturamento_total = sum(produto['qtd'] * produto['preco_venda'] for produto in estoque)
    print(f"Custo total: R$ {custo_total:.2f}".rjust(80))
    print(f"Faturamento total: R$ {faturamento_total:.2f}".rjust(80))
    print()
    print("============= Fim do relatório =============".center(80))
    print()

def menu(): #Requisito 5
    #A função estoque_esta_vazio estava sendo utilizada diversas vezes para verificar se o estoque está vazio antes de realizar alguma operação, embora o AT já conte com um estoque inicial. Mesmo assim eu pensei que seria interessante fazer a validação antes de realizar alguma operação (caso o usuário tenha removido todos os produtos por exemplo).
    #Pensando nisso criei uma verificação para o estoque vazio antes de realizar todas as operações exceto a de cadastro de produto.
    '''
    Função que exibe o menu de opções para o usuário

    return: None
    '''
    while True:
        print("============= Menu =============".center(80))
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Ordenar produtos por quantidade")
        print("4 - Buscar produto")
        print("5 - Remover produto com base no código")
        print("6 - Consulta de produtos esgotados")
        print("7 - Consulta de produtos com baixa quantidade")
        print("8 - Atualizar estoque")
        print("9 - Atualizar preço de venda")
        print("10 - Calcular o valor total do estoque")
        print("11 - Calcular o lucro presumido do estoque")
        print("12 - Relatório geral do estoque\n")
        print("0 - Sair")
        print("============= Fim do menu =============".center(80))
        opcao = input("Escolha uma opção: ")
        if opcao in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            if estoque_esta_vazio(estoque):
                print("Retornando ao menu. Utilize a opção 1 para cadastrar um produto antes de continuar")
                continue
        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            ordenar_produtos_por_quantidade()
        elif opcao == "4":
            while True:
                escolha = input("Deseja buscar por descrição [1] ou código [2]? ")
                if escolha == "1":
                    descricao = input("Digite a descrição do produto: ")
                    buscar_produto(escolha, descricao.strip())
                    break
                elif escolha == "2":
                    codigo = input("Digite o código do produto: ")
                    buscar_produto(escolha, codigo.strip())
                    break
                else:
                    print("Opção inválida! Tente novamente")
        elif opcao == "5":
            remover_produto(estoque)
        elif opcao == "6":
            consulta_produtos_esgotados(estoque)
        elif opcao == "7":
            while True:
                quantidade = input("Digite a quantidade mínima de produtos (Para utilizar a quantidade padrão 'menor que 10' deixe em branco): ")
                if quantidade.isnumeric():
                    produtos_com_baixa_quantidade(estoque, int(quantidade))
                    break
                elif quantidade == "":
                    produtos_com_baixa_quantidade(estoque)
                    break
                print("Quantidade inválida! Tente novamente")
        elif opcao == "8":
            while True:
                operacao = input("Deseja:\n[1] adicionar produtos do estoque?\n[2] remover produtos do estoque?\n")
                if operacao == "2":
                    atualizar_estoque(estoque, "remover")
                    break
                elif operacao == "1":
                    atualizar_estoque(estoque, "adicionar")
                    break
                else:
                    print("Opção inválida! Tente novamente")
        elif opcao == "9":
            atualizar_preco_venda(estoque)
        elif opcao == "10":
            calcular_valor_total_estoque(estoque)
        elif opcao == "11":
            calcular_lucro_presumido_estoque(estoque)
        elif opcao == "12":
            relatorio_geral_estoque(estoque)        
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

if __name__ == '__main__':
    estoque = criar_estoque(estoque_inicial)
    menu()