## Gerenciador de Biblioteca

# Poderá adicionar livros, listar todos os livros disponíveis e buscar um livro pelo título.

def adicionar_livro(livros, titulo, autor):
    '''
    Função para adicionar um livro à lista de livros
    '''
    livro = { "Título": titulo, "Autor": autor }
    livros.append(livro)

def listar_livros(livros):
    '''
    Recebe uma lista e imprime todos os livros da biblioteca
    '''
    if not livros:
        print("Não há livros na biblioteca")
    for livro in livros:
        print(f"Título: {livro['Título']}, Autor: {livro['Autor']}")

def buscar_livro(livros, titulo):
    '''
    Função para buscar um livro pelo título
    '''
    for livro in livros:
        if livro["Título"].lower() == titulo.lower():
            print(f"O livro {titulo} foi escrito por {livro['Autor']} FOI ENCONTRADO!")
            return # achou o livro, sai da função
    print(f"O livro {titulo} não foi encontrado")

def buscar_autor(livros, autor):
    '''
    Função para buscar um livro pelo autor
    '''
    for livro in livros:
        if livro["Autor"].lower() == autor.lower():
            print(f"O livro {livro['Título']} foi escrito por {autor} FOI ENCONTRADO!")
            return # achou o livro, sai da função
    print(f"O autor {autor} não foi encontrado")


def menu():
    '''
    Função para exibir o menu de opções
    '''
    livros = []
    while True:
        escolha = input("Escolha entre adicionar um livro [1], listar os livros [2], buscar livro pelo título [3], buscar livro pelo autor [4] ou sair do programa [0]\n")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")

            adicionar_livro(livros, titulo, autor)
            print("Livro adicionado com sucesso!")

        elif escolha == "2":
            listar_livros(livros)
        
        elif escolha == "3":
            titulo = input("Digite o título do livro que deseja buscar: ")
            buscar_livro(livros, titulo)

        elif escolha == "4":
            autor = input("Digite o autor do livro que deseja buscar: ")
            buscar_autor(livros, autor)

        elif escolha == "0":
            print("Saindo do programa...")
            break
        
  
menu()

