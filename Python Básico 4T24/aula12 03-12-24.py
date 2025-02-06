receitas = []

def menu():
    while True:
        print('\n======Sistema de Gerenciamento de Receitas======')
        print('1. Adicionar receita')
        print('2. Listar todas as receitas')
        print('3. Garantir que todas as receitas possuam um ingrediente específico')
        print('4. Buscar receita com um ingrediente específico')
        print('5. Filtrar receitas por alguma categoria específica')
        print('6. Ordenar receitas')
        print('7. Transformar nomes de receitas para maiúsculas')
        print('8. Sair do programa')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            adicionar_receita()
        elif opcao == '2':
            listar_receitas()
        elif opcao == '3':
            garantir_receita_com_ingrediente()
        elif opcao == '4':
            buscar_receita_com_ingrediente()
        elif opcao == '5':
            print('Função ainda não implementada')
        elif opcao == '6':
            print('Função ainda não implementada')
        elif opcao == '7':
            print('Função ainda não implementada')
        elif opcao == '8':
            print('Saindo do programa...')
            break

def adicionar_receita():
    '''
    Função para adicionar uma nova receita ao sistema
    '''
    nome = input('Digite o nome da receita: ')
    ingredientes = input('Digite os ingredientes da receita separados por vírgula: ').split(', ')
    categoria = input('Digite a categoria da receita: ')

    receitas.append({'nome': nome, 'ingredientes': ingredientes, 'categoria': categoria})
    print(f'Receita {nome} adicionada com sucesso!')


def listar_receitas():
    '''
    Função para listar todas as receitas cadastradas no sistema
    '''
    if not receitas:
        print('Nenhuma receita cadastrada no sistema')
        return
    print('======Lista de Receitas======')
    for receita in receitas:
        print(f'\nNome: {receita["nome"]}')
        print(f'Ingredientes: {", ".join(receita["ingredientes"])}')
        print(f'Categoria: {receita["categoria"]}') 

def garantir_receita_com_ingrediente():
    '''
    Função para garantir que todas as receitas possuam um ingrediente específico
    '''
    ingrediente = input('Digite o ingrediente que deseja verificar: ')
    resultado = all(ingrediente in receita['ingredientes'] for receita in receitas)
    print('Todas as receitas possuem o ingrediente' if resultado else 'Algumas receitas não possuem o ingrediente')

def buscar_receita_com_ingrediente():
    '''
    Função para buscar uma receita que possua um ingrediente específico
    '''
    if not receitas:
        print('Nenhuma receita cadastrada no sistema')
        return
    ingrediente = input('Digite o ingrediente que deseja buscar: ')
    resultado = any(ingrediente in receita['ingredientes'] for receita in receitas)
    print(f"Alguma receita possui o ingrediente '{ingrediente}'" if resultado else f"Nenhuma receita possui o ingrediente '{ingrediente}'")
        
if __name__ == '__main__':
    menu()

#para que serve if __name__ == '__main__':?
#caso eu importe esse arquivo em outro arquivo, o código dentro do if não será executado. Se eu executar esse arquivo diretamente, o código dentro do if será executado. Isso é útil para testar o código de um arquivo sem executar o código de inicialização, por exemplo.

'''
receitas = [
    {"nome": "Bolo de cenoura", "ingredientes": ["cenoura", "ovo", "farinha", "açúcar"], "categoria": "sobremesa"},
    {"nome": "Arroz", "ingredientes": ["arroz", "sal"], "categoria": "prato principal"},
    {"nome": "Brigadeiro", "ingredientes": ["leite condensado", "manteiga", "chocolate", "açúcar"], "categoria": "sobremesa"},
    {"nome": "Feijoada", "ingredientes": ["feijão", "carne de porco", "sal"], "categoria": "prato principal"},
    {"nome": "Salada de frutas", "ingredientes": ["banana", "maçã", "laranja"], "categoria": "sobremesa"},
    {"nome": "Sopa de legumes", "ingredientes": ["cenoura", "batata", "abóbora", "sal"], "categoria": "prato principal"}
]'''


