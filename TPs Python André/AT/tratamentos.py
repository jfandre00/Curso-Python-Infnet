#Todas as validações estão nesse arquivo

def variavel_vazia(variavel):
    '''
    Função que verifica se uma variável é vazia

    variavel: str

    return: bool
    '''
    if variavel == "": 
        return True
    return False

def codigo_existe(codigo, estoque):
    '''
    Função que verifica se um código de produto já existe

    codigo: int
    estoque: list

    return: bool
    '''
    for produto in estoque:
        if produto['codigo'] == codigo:
            return True
    return False

def obter_input_valido(mensagem, condicao, mensagem_erro):
    '''
    Função que obtém um input válido

    mensagem: str
    condicao: function
    mensagem_erro: str

    return: str
    '''
    while True:
        variavel = input(mensagem)
        if condicao(variavel):
            print(mensagem_erro)
        else:
            return variavel
    
def estoque_esta_vazio(estoque):
    '''
    Função que verifica se o estoque está vazio

    estoque: list

    return: bool
    '''
    if len(estoque) == 0:
        print("Estoque vazio")
        return True
    return False

def gerar_print_produto(produto):
    '''
    Função que gera o print de um produto

    produto: dict

    return: None
    '''
    print(f"{produto['nome']} - Código: {produto['codigo']} - Qtd: {produto['qtd']} - Preço de custo: R$ {produto['preco_custo']:.2f} - Preço de venda: R$ {produto['preco_venda']:.2f}")

#Requisito 12  
def validar_estoque_ou_preco(estoque=None, codigo=None, numero=None, preco_venda=None, preco_custo=None): 
    '''
    Função que valida a atualização do estoque ou o preço de venda.

    estoque: list (opcional)
    codigo: int (opcional)
    numero: int (opcional)
    preco_venda: float (opcional)
    preco_custo: float (opcional)

    return: bool
    '''
    if estoque is not None and codigo is not None and numero is not None:
        # Validação do estoque
        for produto in estoque:
            if produto['codigo'] == codigo:
                if produto['qtd'] >= numero:
                    return True
                else:
                    print("Quantidade indisponível")
                    return False
    
    if preco_venda is not None and preco_custo is not None:
        # Validação do preço
        if preco_venda < preco_custo:
            print("Preço de venda deve ser maior ou igual ao preço de custo")
            return False
        return True
    
    print("Parâmetros insuficientes para validação")
    return False