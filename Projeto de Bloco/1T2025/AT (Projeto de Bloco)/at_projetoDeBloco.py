import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import os
from datetime import datetime

# URL do site para web scraping
url = "https://pedrovncs.github.io/livrariapython/livros.html"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# Extrai informações dos livros
livros = soup.find_all('li', class_='list-group-item')
dados_livros = []
dados_autores = set()
dados_livro_autor = []

for livro in livros:
    titulo = livro.find('h5').text.strip()
    info = livro.find_all('p')
    isbn = info[0].text.replace('ISBN:', '').strip()
    genero = info[1].text.replace('Gênero:', '').strip()
    autores = info[2].text.replace('Autor(es):', '').strip()
    pais = info[3].text.replace('País de Nascimento:', '').strip()
    data_pub = info[4].text.replace('Data de publicação:', '').strip()
    paginas = int(info[5].text.replace('Páginas:', '').strip())
    quantidade = int(info[6].text.replace('Quantidade Disponível:', '').strip())

    from dateutil import parser
    data_formatada = parser.parse(data_pub).strftime('%Y-%m-%d')

    dados_livros.append((isbn, titulo, genero, data_formatada, paginas, quantidade))

    lista_autores = [autor.strip() for autor in autores.split(',')]
    for autor in lista_autores:
        dados_autores.add((autor, pais))
        dados_livro_autor.append((isbn, autor))

# Remover o banco se já existir
if os.path.exists('biblioteca_tp5.db'):
    os.remove('biblioteca_tp5.db')

# Criação do banco de dados SQLite
conn = sqlite3.connect('biblioteca_tp5.db')
cursor = conn.cursor()

# Criação das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    isbn TEXT PRIMARY KEY,
    titulo TEXT,
    genero TEXT,
    data_publicacao DATE,
    paginas INTEGER,
    quantidade_disponivel INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    pais TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS livro_autor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn TEXT,
    id_autor INTEGER,
    FOREIGN KEY (isbn) REFERENCES livros (isbn),
    FOREIGN KEY (id_autor) REFERENCES autores (id_autor)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS emprestimos (
    id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER,
    isbn TEXT,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
    FOREIGN KEY (isbn) REFERENCES livros (isbn)
)
''')

# Inserção dos dados dos livros e autores
cursor.executemany('''
INSERT OR IGNORE INTO livros (isbn, titulo, genero, data_publicacao, paginas, quantidade_disponivel)
VALUES (?, ?, ?, ?, ?, ?)
''', dados_livros)

for autor, pais in dados_autores:
    cursor.execute('''
    INSERT OR IGNORE INTO autores (nome, pais) VALUES (?, ?)
    ''', (autor, pais))

for isbn, autor in dados_livro_autor:
    cursor.execute('''
    INSERT INTO livro_autor (isbn, id_autor)
    SELECT ?, id_autor FROM autores WHERE nome = ?
    ''', (isbn, autor))

conn.commit()

# Função para registrar ações no arquivo Excel
log_file = 'log_biblioteca.xlsx'
log_data = []

def registrar_log(acao, detalhes):
    global log_data
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_data.append({'Data': data_hora, 'Ação': acao, 'Detalhes': detalhes})

# Funções de gerenciamento
def cadastrar_usuario(nome):
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    if cursor.fetchone():
        print(f'Usuário "{nome}" já está cadastrado.')
    else:
        cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
        conn.commit()
        registrar_log('Cadastro de Usuário', f'Usuário "{nome}" cadastrado com sucesso.')

def emprestar_livro(nome_usuario, isbn):
    cursor.execute('SELECT id_usuario FROM usuarios WHERE nome = ?', (nome_usuario,))
    usuario = cursor.fetchone()

    if not usuario:
        print(f'Usuário "{nome_usuario}" não encontrado.')
        return
    
    id_usuario = usuario[0]
    
    # Verifica quantos livros o usuário já tem emprestados
    cursor.execute('''
        SELECT COUNT(*) FROM emprestimos 
        WHERE id_usuario = ? AND data_devolucao IS NULL
    ''', (id_usuario,))
    qtd_emprestados = cursor.fetchone()[0]
    
    if qtd_emprestados >= 5:
        print(f'Usuário "{nome_usuario}" já atingiu o limite de 5 livros.')
        return

    # Verifica se o livro está disponível
    cursor.execute('SELECT titulo, quantidade_disponivel FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()

    if not livro:
        print('Livro não encontrado.')
        return
    
    titulo, quantidade = livro
    if quantidade > 0:
        cursor.execute('''
            INSERT INTO emprestimos (id_usuario, isbn, data_emprestimo) 
            VALUES (?, ?, ?)
        ''', (id_usuario, isbn, datetime.now().strftime('%Y-%m-%d')))
        
        cursor.execute('UPDATE livros SET quantidade_disponivel = quantidade_disponivel - 1 WHERE isbn = ?', (isbn,))
        conn.commit()
        registrar_log('Empréstimo', f'Livro "{titulo}" emprestado para "{nome_usuario}".')
        print(f'Livro "{titulo}" emprestado com sucesso!')
    else:
        print(f'Livro "{titulo}" está indisponível no momento.')

def devolver_livro(nome_usuario, isbn):
    cursor.execute('SELECT id_usuario FROM usuarios WHERE nome = ?', (nome_usuario,))
    usuario = cursor.fetchone()

    if not usuario:
        print(f'Usuário "{nome_usuario}" não encontrado.')
        return

    id_usuario = usuario[0]

    cursor.execute('''
        SELECT id_emprestimo FROM emprestimos 
        WHERE id_usuario = ? AND isbn = ? AND data_devolucao IS NULL
    ''', (id_usuario, isbn))
    
    emprestimo = cursor.fetchone()
    
    if emprestimo:
        cursor.execute('''
            UPDATE emprestimos 
            SET data_devolucao = ?
            WHERE id_emprestimo = ?
        ''', (datetime.now().strftime('%Y-%m-%d'), emprestimo[0]))
        
        cursor.execute('UPDATE livros SET quantidade_disponivel = quantidade_disponivel + 1 WHERE isbn = ?', (isbn,))
        conn.commit()
        registrar_log('Devolução', f'Livro "{isbn}" devolvido por "{nome_usuario}".')
        print('Livro devolvido com sucesso!')
    else:
        print('Empréstimo não encontrado.')

# Menu da aplicação
def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Empréstimos ===")
        print("1. Cadastrar Usuário")
        print("2. Emprestar Livro")
        print("3. Devolver Livro")
        print("4. Sair e Salvar Log")
        print("5. Consultar o Estoque de Livros")
        print("6. Consultar os Empréstimos Atuais")
        print("7. Consultar os Usuários Cadastrados")
        print("8. Consultar os Autores Cadastrados")
        print("9. Consultar os Livros por Autor")
        print("10. Consultar os Livros por Gênero")
        print("11. Consultar os Livros Disponíveis")
        print("12. Consultar os Livros Emprestados")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input('Digite o nome do usuário: ')
            cadastrar_usuario(nome)
        
        elif opcao == '2':
            nome = input('Digite o nome do usuário: ')
            isbn = input('Digite o ISBN do livro: ')
            emprestar_livro(nome, isbn)
        
        elif opcao == '3':
            nome = input('Digite o nome do usuário: ')
            isbn = input('Digite o ISBN do livro: ')
            devolver_livro(nome, isbn)
        
        elif opcao == '4':
            df_log = pd.DataFrame(log_data)
            df_log.to_excel(log_file, index=False)
            print(f'Log salvo em "{log_file}".')
            break
        
        elif opcao == '5':
            cursor.execute('SELECT * FROM livros')
            livros = cursor.fetchall()
            print("Estoque de Livros:")
            for livro in livros:
                print(livro)
            
        elif opcao == '6':
            cursor.execute('''
                SELECT u.nome, l.titulo, e.data_emprestimo 
                FROM emprestimos e 
                JOIN usuarios u ON e.id_usuario = u.id_usuario 
                JOIN livros l ON e.isbn = l.isbn 
                WHERE e.data_devolucao IS NULL
            ''')
            emprestimos = cursor.fetchall()
            print("Empréstimos Atuais:")
            for emp in emprestimos:
                print(emp)

        elif opcao == '7':
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            print("Usuários Cadastrados:")
            for usuario in usuarios:
                print(usuario)

        elif opcao == '8':
            cursor.execute('SELECT * FROM autores')
            autores = cursor.fetchall()
            print("Autores Cadastrados:")
            for autor in autores:
                print(autor)

        elif opcao == '9':
            autor = input('Digite o nome do autor: ')
            cursor.execute('''
                SELECT l.titulo 
                FROM livro_autor la 
                JOIN livros l ON la.isbn = l.isbn 
                JOIN autores a ON la.id_autor = a.id_autor 
                WHERE a.nome = ?
            ''', (autor,))
            livros_autor = cursor.fetchall()
            print(f"Livros do Autor '{autor}':")
            for livro in livros_autor:
                print(livro)

        elif opcao == '10':
            genero = input('Digite o gênero: ')
            cursor.execute('SELECT * FROM livros WHERE genero = ?', (genero,))
            livros_genero = cursor.fetchall()
            print(f"Livros do Gênero '{genero}':")
            for livro in livros_genero:
                print(livro)

        elif opcao == '11':
            cursor.execute('SELECT * FROM livros WHERE quantidade_disponivel > 0')
            livros_disponiveis = cursor.fetchall()
            print("Livros Disponíveis:")
            for livro in livros_disponiveis:
                print(livro)

        elif opcao == '12':
            cursor.execute('''
                SELECT l.titulo, u.nome 
                FROM emprestimos e 
                JOIN livros l ON e.isbn = l.isbn 
                JOIN usuarios u ON e.id_usuario = u.id_usuario 
                WHERE e.data_devolucao IS NULL
            ''')
            livros_emprestados = cursor.fetchall()
            print("Livros Emprestados:")
            for livro in livros_emprestados:
                print(livro)
        
        else:
            print('Opção inválida!')

# Executa o menu
menu()
