# TP5 Projeto de Bloco - 2025 - André L M Ferreira

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import os

# URL do site do TP5
url = "https://pedrovncs.github.io/livrariapython/livros.html"

# Obtenção do HTML da página
response = urllib.request.urlopen(url)
html = response.read()

# Analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontra todos os livros
livros = soup.find_all('li', class_='list-group-item')

'''
Acima, temos uma lista de livros, onde cada livro é um objeto do tipo 'li' com a classe 'list-group-item'. Dentro de cada livro, temos um título (h5) e uma lista de informações (p).
Cada p tem o formato:
<p class="mb-0"><strong>Gênero:</strong> Ficção Científica</p>
<p class="mb-0"><strong>Autor(es):</strong> Arkady Strugatsky, Boris Strugatsky</p>
<p class="mb-0"><strong>País de Nascimento:</strong> Rússia, Rússia</p>
<p class="mb-0"><strong>Data de publicação:</strong> 01-01-1972</p>
<p class="mb-0"><strong>Páginas:</strong> 224</p>
<p class="mb-0"><strong>Quantidade Disponível:</strong> 2</p>
Vamos iterar por cada <li> e buscar os <p> dentro. Irá retornar uma lista de <p> com as informações do livro, estamos chamando de 'info'.

Para inserirmos o título, vamos pegar o texto do h5 e remover os espaços em branco com strip(). O título também está dentro de cada <li>.
'''

# Lista para armazenar os dados dos livros
dados_livros = []
dados_autores = set()  # Usando set para evitar autores duplicados
dados_livro_autor = []


# Vamos extrair as informações de cada livro
for livro in livros:
    titulo = livro.find('h5').text.strip() # Encontra o título do livro e remove os espaços em branco.
    
    info = livro.find_all('p') # Encontra todas as informações do livro e abaixo vamos separar cada informação em variáveis.
    isbn = info[0].text.replace('ISBN:', '').strip()
    genero = info[1].text.replace('Gênero:', '').strip()
    autores = info[2].text.replace('Autor(es):', '').strip()
    pais = info[3].text.replace('País de Nascimento:', '').strip()
    data_pub = info[4].text.replace('Data de publicação:', '').strip()
    paginas = int(info[5].text.replace('Páginas:', '').strip())
    quantidade = int(info[6].text.replace('Quantidade Disponível:', '').strip())
    
    # Vamos converter a data para o formato "ano-mes-dia", conforme enunciado
    # Tentei usar o pandas.to_datetime, mas não funcionou com o formato da data
    # Tentei também usar o datetime.strptime, mas também não funcionou com o formato da data
    # Por fim, encontrei a biblioteca dateutil que consegue fazer o parse da data, após pesquisar no StackOverflow.

    from dateutil import parser
    data_formatada = parser.parse(data_pub).strftime('%Y-%m-%d')

    # Adiciona os dados do livro
    dados_livros.append((isbn, titulo, genero, data_formatada, paginas, quantidade))

    # Adiciona autores (tratamento para vários autores separados por vírgula)
    lista_autores = [autor.strip() for autor in autores.split(',')]
    for autor in lista_autores:
        dados_autores.add((autor, pais))
        dados_livro_autor.append((isbn, autor))

# Criação do DataFrame para os livros
colunas_livros = ['ISBN', 'Titulo', 'Genero', 'Data_Publicacao', 'Paginas', 'Quantidade_Disponivel']
df_livros = pd.DataFrame(dados_livros, columns=colunas_livros)

colunas_autores = ['Nome', 'Pais']
df_autores = pd.DataFrame(list(dados_autores), columns=colunas_autores)

colunas_livro_autor = ['ISBN', 'Nome_Autor']
df_livro_autor = pd.DataFrame(dados_livro_autor, columns=colunas_livro_autor)

#Se o arquivo já existir, deleta, pois quando estou rodando o código várias vezes, insere os dados duplicados, triplicados, etc.
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

# Inserção dos dados em livros
cursor.executemany('''
INSERT OR IGNORE INTO livros (isbn, titulo, genero, data_publicacao, paginas, quantidade_disponivel)
VALUES (?, ?, ?, ?, ?, ?)
''', dados_livros)

# Inserção dos dados em autores
for _, row in df_autores.iterrows():
    cursor.execute('''
    INSERT OR IGNORE INTO autores (nome, pais) VALUES (?, ?)
    ''', (row['Nome'], row['Pais']))

# Inserção dos dados em livro_autor
for _, row in df_livro_autor.iterrows():
    cursor.execute('''
    INSERT INTO livro_autor (isbn, id_autor)
    SELECT ?, id_autor FROM autores WHERE nome = ?
    ''', (row['ISBN'], row['Nome_Autor']))

# Confirma as inserções e fecha a conexão
conn.commit()

# Consulta para validar os dados inseridos
print("Livros:\n", pd.read_sql_query("SELECT * FROM livros", conn))
print("\nAutores:\n", pd.read_sql_query("SELECT * FROM autores", conn))
print("\nRelacionamento Livro-Autor:\n", pd.read_sql_query("SELECT * FROM livro_autor", conn))

# #######################################################################
print("\nConsultas Adicionais para confirmarmos os dados inseridos:")
# #######################################################################

# 1. Consultar os autores que tem mais de um livro escrito

print("Autores que tem mais de um livro escrito:\n", pd.read_sql_query('''
SELECT a.nome, COUNT(*) as qtd_livros
FROM autores a
JOIN livro_autor la ON a.id_autor = la.id_autor
GROUP BY a.nome
HAVING COUNT(*) > 1
''', conn))

# 2. Consultar os livros que tem mais de um autor
print("Livros que tem mais de um autor:\n", pd.read_sql_query('''
SELECT isbn, COUNT(*) as qtd_autores
FROM livro_autor
GROUP BY isbn
HAVING COUNT(*) > 1
''', conn))

# 3. Consultar quantos livros temos disponíveis
print("Quantidade de livros disponíveis:\n", pd.read_sql_query('''
SELECT SUM(quantidade_disponivel) as total_livros
FROM livros
''', conn).to_string(index=False))

# 4. Consultar a quantidade de livros por gênero
print("Quantidade de livros por gênero:\n", pd.read_sql_query('''
SELECT genero, COUNT(*) as qtd_livros 
FROM livros 
GROUP BY genero
''', conn))

# 5. Consultar o gênero do livro e quantidade de livros disponíveis
print("Gênero do livro e quantidade de livros disponíveis:\n", pd.read_sql_query('''
SELECT genero, SUM(quantidade_disponivel) as total_livros
FROM livros
GROUP BY genero
''', conn))

# 6. Agrupar os livros por quantidade de páginas. Até 200 páginas, de 201 a 400 páginas, de 401 a 600 páginas e acima de 600 páginas.
print("Agrupamento de livros (títulos) por quantidade de páginas:\n", pd.read_sql_query('''
SELECT 
    CASE 
        WHEN paginas <= 200 THEN '1. Até 200 páginas'
        WHEN paginas <= 400 THEN '2. De 201 a 400 páginas'
        WHEN paginas <= 600 THEN '3. De 401 a 600 páginas'
        ELSE '4. Acima de 600 páginas'
    END as grupo_paginas,
    COUNT(*) as qtd_titulos
FROM livros
GROUP BY grupo_paginas
''', conn).to_string(index=False))

# 7. Quais são os livros escritos por autores brasileiros?
print("Livros escritos por autores brasileiros:\n", pd.read_sql_query('''
SELECT l.titulo, a.nome, a.pais
FROM livros l
JOIN livro_autor la ON l.isbn = la.isbn
JOIN autores a ON la.id_autor = a.id_autor
WHERE a.pais = 'Brasil'
''', conn))

# 8. Consulta todos os livros e seus autores
print("Livros e seus autores:\n", pd.read_sql_query('''
SELECT l.titulo, a.nome, a.pais
FROM livros l
JOIN livro_autor la ON l.isbn = la.isbn
JOIN autores a ON la.id_autor = a.id_autor
''', conn))


conn.close()