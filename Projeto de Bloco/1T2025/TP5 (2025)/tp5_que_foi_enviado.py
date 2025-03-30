# TP5 Projeto de Bloco - 2025 - André L M Ferreira

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import os
from dateutil import parser # Importando a biblioteca dateutil para fazer o parse da data

# Função para exibir resultados formatados
def print_query(title, query, conn):
    print(f"\n=== {title.upper()} ===")
    print(pd.read_sql_query(query, conn).to_string(index=False))
    print("\n" + "="*50 + "\n")

# URL do site do TP5
url = "https://pedrovncs.github.io/livrariapython/livros.html"

# Obter o código HTML da página
response = urllib.request.urlopen(url)
html = response.read()

# Analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontra todos os livros, determinando o elemento <li> com a classe 'list-group-item' após fazer a inspeção do HTML.
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

# Listas para armazenar os dados
dados_livros = []
dados_autores = set() # Usando set para evitar autores duplicados
dados_livro_autor = []

# Extrair informações de cada livro
for livro in livros:
    titulo = livro.find('h5').text.strip() # além de remover os espaços em branco, já estamos pegando o título do livro.
    info = livro.find_all('p') # Encontra todas as informações do livro e abaixo vamos separar cada informação em variáveis diferentes, já fazendo a conversão de tipo.
    
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

    data_formatada = parser.parse(data_pub).strftime('%Y-%m-%d')

    # Adiciona dados do livro 
    dados_livros.append((titulo, isbn, genero, data_formatada, paginas, quantidade))

    # Adiciona autores (tratamento para vários autores separados por vírgula)
    lista_autores = [autor.strip() for autor in autores.split(',')]
    for autor in lista_autores:
        dados_autores.add((autor, pais))
        dados_livro_autor.append((isbn, autor))  # Temporariamente usando ISBN

# Criação dos DataFrames
df_livros = pd.DataFrame(dados_livros, columns=['Titulo', 'ISBN', 'Genero', 'Data_Publicacao', 'Paginas', 'Quantidade_Disponivel'])
df_autores = pd.DataFrame(list(dados_autores), columns=['Nome', 'Pais'])
df_livro_autor = pd.DataFrame(dados_livro_autor, columns=['ISBN', 'Nome_Autor'])

#Se o arquivo já existir, deleta, pois quando estou rodando o código várias vezes, insere os dados duplicados, triplicados, etc.
if os.path.exists('biblioteca_tp5_final.db'):
    os.remove('biblioteca_tp5_final.db')

# Criação do banco de dados SQLite
conn = sqlite3.connect('biblioteca_tp5_final.db')
cursor = conn.cursor()

# Criação das tabelas 
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    isbn TEXT UNIQUE NOT NULL,
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
    id_livro INTEGER,
    id_autor INTEGER,
    PRIMARY KEY (id_livro, id_autor),
    FOREIGN KEY (id_livro) REFERENCES livros (id_livro),
    FOREIGN KEY (id_autor) REFERENCES autores (id_autor)
)
''')

# Inserção dos dados em livros (irá gerar id_livro automaticamente)
cursor.executemany('''
INSERT INTO livros (titulo, isbn, genero, data_publicacao, paginas, quantidade_disponivel)
VALUES (?, ?, ?, ?, ?, ?)
''', dados_livros)

# Inserção dos autores
for _, row in df_autores.iterrows():
    cursor.execute('INSERT OR IGNORE INTO autores (nome, pais) VALUES (?, ?)', 
                  (row['Nome'], row['Pais']))

# Obter mapeamento ISBN utilizando dicionários -> id_livro. Vamos usar o ISBN para pegar o id_livro, pois ele é único.
cursor.execute('SELECT id_livro, isbn FROM livros')
isbn_to_id = {isbn: id_livro for id_livro, isbn in cursor.fetchall()}

# Obter mapeamento nome utilizando dicionários -> id_autor. Vamos usar o nome do autor para pegar o id_autor, pois ele é único.
cursor.execute('SELECT id_autor, nome FROM autores')
nome_to_id = {nome: id_autor for id_autor, nome in cursor.fetchall()}

# Inserir relacionamentos usando id_livro e id_autor
for _, row in df_livro_autor.iterrows():
    id_livro = isbn_to_id.get(row['ISBN'])
    id_autor = nome_to_id.get(row['Nome_Autor'])
    if id_livro and id_autor: # Verifica se ambos os IDs foram encontrados
        cursor.execute('INSERT OR IGNORE INTO livro_autor (id_livro, id_autor) VALUES (?, ?)', 
                      (id_livro, id_autor))

# Confirma as inserções e fecha a conexão
conn.commit()


# Algumas consultas usando a função print_query que criei acima

print_query("Todos os livros e seus autores", '''
SELECT l.titulo, a.nome as autor, a.pais, l.genero, l.paginas
FROM livros l
JOIN livro_autor la ON l.id_livro = la.id_livro
JOIN autores a ON la.id_autor = a.id_autor
ORDER BY l.titulo, a.nome
''', conn)


print_query("Autores com mais de um livro escrito", '''
SELECT a.nome, COUNT(*) as qtd_livros
FROM autores a
JOIN livro_autor la ON a.id_autor = la.id_autor
GROUP BY a.nome
HAVING COUNT(*) > 1
ORDER BY qtd_livros DESC
''', conn)

print_query("Livros com mais de um autor", '''
SELECT l.titulo, COUNT(*) as qtd_autores
FROM livros l
JOIN livro_autor la ON l.id_livro = la.id_livro
GROUP BY l.id_livro, l.titulo
HAVING COUNT(*) > 1
ORDER BY qtd_autores DESC
''', conn)

print_query("Quantidade total de livros disponíveis", '''
SELECT SUM(quantidade_disponivel) as total_livros_disponiveis
FROM livros
''', conn)

print_query("Quantidade de livros por gênero", '''
SELECT genero, COUNT(*) as quantidade_livros
FROM livros
GROUP BY genero
ORDER BY quantidade_livros DESC
''', conn)

print_query("Livros disponíveis por gênero", '''
SELECT genero, SUM(quantidade_disponivel) as exemplares_disponiveis
FROM livros
GROUP BY genero
ORDER BY exemplares_disponiveis DESC
''', conn)

print_query("Livros por faixa de páginas", '''
SELECT 
    CASE 
        WHEN paginas <= 200 THEN '1. Até 200 páginas'
        WHEN paginas <= 400 THEN '2. 201-400 páginas'
        WHEN paginas <= 600 THEN '3. 401-600 páginas'
        ELSE '4. Acima de 600 páginas'
    END as faixa_paginas,
    COUNT(*) as quantidade_livros,
    SUM(quantidade_disponivel) as exemplares_disponiveis
FROM livros
GROUP BY faixa_paginas
ORDER BY faixa_paginas
''', conn)

print_query("Livros escritos por autores brasileiros", '''
SELECT l.titulo, a.nome, a.pais, l.quantidade_disponivel
FROM livros l
JOIN livro_autor la ON l.id_livro = la.id_livro
JOIN autores a ON la.id_autor = a.id_autor
WHERE a.pais = 'Brasil'
ORDER BY l.titulo
''', conn)

conn.close()


