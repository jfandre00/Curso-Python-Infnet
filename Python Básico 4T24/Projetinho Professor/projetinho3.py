#receitas = []

receitas = [
    {'nome': 'Bolo de cenoura', 'ingredientes': ['cenoura', 'açúcar', 'farinha', 'ovo', 'fermento'], 'categoria': 'sobremesa'},
    {'nome': 'Bolo de chocolate', 'ingredientes': ['chocolate', 'açúcar', 'farinha', 'ovo'], 'categoria': 'sobremesa'},
    {'nome': 'Arroz', 'ingredientes': ['arroz', 'sal'], 'categoria': 'prato principal'},
    {'nome': 'Feijão', 'ingredientes': ['feijão', 'sal', 'bacon'], 'categoria': 'prato principal'},
    {'nome': 'Brigadeiro', 'ingredientes': ['leite condensado', 'manteiga', 'chocolate', 'açúcar', 'chocolate granulado', 'leite'], 'categoria': 'sobremesa'}
]

def adicionar_receita():
    '''
    Função para adicionar uma receita à lista de receitas
    '''
    nome = input("Digite o nome da receita: ")
    ingredientes = input("Digite os ingredientes separados por vírgula: ")
    categoria = input("Digite a categoria (ex: sobremesa, prato principal): ")
    receita = {
        "nome": nome,
        "ingredientes": ingredientes.split(', '),
        "categoria": categoria
    }
    receitas.append(receita)
    print(f"\nReceita {receita['nome']} adicionada com sucesso!\n")

def listar_receitas():
    if not receitas:
        print('Nenhuma receita cadastrada')
        return
    print("\n=== Lista de receitas ===")
    for i, receita in enumerate(receitas, 1):
        print(f"{i}. {receita['nome']} ({len(receita['ingredientes'])} ingredientes) - {receita['categoria']}")
    print('\n')

def todas_tem_ingrediente():
    ingrediente = input("Digite o ingrediente para buscar: ")
    resultado = all(ingrediente in receita['ingredientes'] for receita in receitas)
    print(f"Todas as receitas possuem {ingrediente}? {'Sim' if resultado else 'Não'}")

def alguma_tem_ingrediente():
    ingrediente = input("Digite o ingrediente para buscar: ")
    resultado = any(ingrediente in receita['ingredientes'] for receita in receitas)
    # if resultado:
    #     print('Sim')
    # else:
    #     print('Não')
    print(f"Alguma receita contém {ingrediente}? {'Sim' if resultado else 'Não'}")

def filtrar_por_categoria():
    categoria = input("Digite a categoria para filtrar: ")
    receitas_filtradas = list(filter(lambda receita: receita['categoria'] == categoria, receitas))
    if not receitas_filtradas:
        print(f"Não há receitas na categoria {categoria}")
        return
    print(f"\n=== Receitas na categoria {categoria} ===")
    for receita in receitas_filtradas:
        print(f"{receita['nome']} ({len(receita['ingredientes'])} ingredientes)")

def ordenar_receitas():
    print("\n1. Ordenar por nome")
    print("2. Ordenar por quantidade de ingredientes (decrescente)")
    print("3. Ordenar por categoria")
    opção = input("Escolha uma opção: ")
    if opção == '1':
        receitas.sort(key=lambda receita: receita['nome'])
        #receitas_ordenadas = sorted(receitas, key=lambda receita: receita['nome'])
    elif opção == '2':
        receitas.sort(key=lambda receita: len(receita['ingredientes']), reverse=True) 
    elif opção == '3':
        receitas.sort(key=lambda receita: receita['categoria'])
    else:
        print("Opção inválida")
        return
    for receita in receitas:
        print(f"{receita['nome']} ({len(receita['ingredientes'])} ingredientes) - {receita['categoria']}")

def transformar_nomes_para_maiúsculas():
    if not receitas:
        print('Nenhuma receita cadastrada')
        return
    nomes_maiusculos = list(map(lambda receita: receita['nome'].upper(), receitas))
    print('Nomes das receitas transformados para maiúsculas')
    print(nomes_maiusculos)

def menu():
    while True:
        print('\n===Sistema de gerenciamento de receitas===')
        print('1. Adicionar receita')
        print('2. Listas todas as receitas')
        print('3. Verificar se todas as receitas possuem um ingrediente específico')
        print('4. Verificar se alguma receita contém um ingrediente específico')
        print('5. Filtrar receitas por alguma categoria específica')
        print('6. Ordenar receitas')
        print('7. Transformar nomes de receitas para maiúsculas')
        print('8. Sair do programa')

        opção = input('Escolha uma opção: ')

        if opção == '1':
            adicionar_receita()
        elif opção == '2':
            listar_receitas()
        elif opção == '3':
            todas_tem_ingrediente()
        elif opção == '4':
            alguma_tem_ingrediente()
        elif opção == '5':
            filtrar_por_categoria()
        elif opção == '6':
            ordenar_receitas()
        elif opção == '7':
            transformar_nomes_para_maiúsculas()
        elif opção == '8':
            print('Até logo!')
            break

if __name__ == "__main__":
    menu()
        
