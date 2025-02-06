def criar_relatorio_estoque(estoque):
    '''
    Cria um relatório de estoque
    '''
    relatorio = []
    for produto in estoque:
        relatorio.append(f"{produto['descricao']} - {produto['quantidade']} unidades")
    return relatorio

#Estoque inicial fornecido pelo enunciado

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

#Converter a string inicial em uma lista de dicionários

def carregar_estoque(estoque_str):
    produtos = []
    for item in estoque_str.split("#"):
        descricao, codigo, quantidade, custo, preco = item.split(";")
        produtos.append({
            "descricao": descricao,
            "codigo": int(codigo),
            "quantidade": int(quantidade),
            "custo": float(custo),
            "preco": float(preco)
        })
    return produtos

estoque = carregar_estoque(estoque_inicial)

#Funcionalidades - 1. Mostrar qual produto tem a maior margem de lucro percentual
#                  2. Mostrar a margem de lucro percentual de todos os produtos
#                  3. Mostrar qual produto tem a menor margem de lucro percentual

#1. Mostrar qual produto tem a maior margem de lucro percentual e mostrar qual a margem mostrada em %

def margem_maior(estoque):
    maior_margem = 0
    produto_maior_margem = None
    for produto in estoque:
        margem = (produto["preco"] - produto["custo"]) / produto["custo"] * 100
        if margem > maior_margem:
            maior_margem = margem
            produto_maior_margem = produto
    print(f"O produto com a maior margem de lucro é {produto_maior_margem['descricao']} com {maior_margem:.2f}%")

produto_maior_margem = margem_maior(estoque)

#2. Mostrar a margem de lucro percentual de todos os produtos

def margem_todos(estoque):
    for produto in estoque:
        margem = (produto["preco"] - produto["custo"]) / produto["custo"] * 100
        print(f"{produto['descricao']} - {margem:.2f}%")
    

margem_todos(estoque)


def ordenar_produtos(estoque, criterio = 'quantidade', ordem='asc'):
    '''
    Ordena os produtos do estoque de acordo com um critério e uma ordem
    '''
    if criterio not in estoque[0].keys():
        return
    return sorted(estoque, key=lambda x: x[criterio], reverse=ordem == 'desc')


estoque_ordenado = ordenar_produtos(estoque, 'quantidade', 'asc')
criar_relatorio_estoque(estoque_ordenado)

