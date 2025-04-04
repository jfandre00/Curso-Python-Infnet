#AT Phyton para Dados 1T25 André L M Ferreira

from bs4 import BeautifulSoup
import urllib.request
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd
import sqlite3
import os

'''
Atenção:
Só consegui o retorno de 25 ocorrências na lista. Isso acontece porque o IMDb carrega a lista dos Top 250 filmes dinamicamente via JavaScript, e o BeautifulSoup não executa JavaScript, então ele só captura os elementos HTML que já estão na página no momento do carregamento inicial. Se quiser capturar todos os 250 filmes, iriamos ter que usar uma ferramenta que execute JavaScript, como o Selenium. Como esse trabalho é sobre BeautifulSoup, vou trabalhar com os 25 filmes que ele consegue capturar.
Fonte: https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python
'''

# Endereço do IMDb Top 250
site = "https://www.imdb.com/chart/top/"

#1. Extrair os filmes do ranking do IMDb
#1.a Acesse a página IMDb top 250, simulando um navegador para evitar bloqueios
req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

filmes = soup.select('li.ipc-metadata-list-summary-item')

#1.b Exibindo os 10 primeiros títulos dos filmes (utilizei o find_all para pegar os títulos)
titulos_ex1b = soup.find_all('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-495ef71a-2 cpvJUg cli-title with-margin')


#1.b Extraia os títulos dos filmes e exiba os 10 primeiros.
print("\n Títulos dos 10 primeiros filmes do IMDb Top 250: \n")
for i in range(10):
    print(titulos_ex1b[i].text.strip())

# Criaremos uma lista de objetos Movie (fiz essa mudança após criar a classe Movie no exercício 3)
movies = []

#2a. Extrair os dados dos filmes do ranking do IMDb

for i, filme in enumerate(filmes, start=1):
    # Título do filme
    titulo_elem = filme.find('h3')
    titulo = titulo_elem.text.strip() if titulo_elem else "N/A"

    # Remover o número do ranking antes do título
    if i < 10:
        titulo = titulo[3:]  # Remove os 3 primeiros caracteres ("1. ")
    else:
        titulo = titulo[4:]  # Remove os 4 primeiros caracteres ("10. ")

    # Tratar o ano do filme
    ano_elem = filme.select_one('.cli-title-metadata-item')
    ano = ano_elem.text.strip() if ano_elem else "N/A"

    # Tratar a nota IMDb
    nota_elem = filme.select_one('.ipc-rating-star--rating')
    nota = nota_elem.text.strip() if nota_elem else "N/A"

    # Criar objeto Movie
    movies.append((titulo, ano, nota))

#2.b Exiba os 5 primeiros filmes formatados. Por exemplo: The Shawshank Redemption (1994) - Nota: 9.2 ou The Godfather (1972) - Nota: 9.1

print("\nOs 5 primeiros filmes do IMDb Top 250:\n")
for i, (titulo, ano, nota) in enumerate(movies[:5], start=1): 
    print(f"{i}. {titulo} ({ano}) - Nota: {nota}")

print("\nFim do exercício 2\n")

#3. Criar a classe base TV e as classes Movie e Serie: Crie uma classe base TV para representar qualquer mídia televisiva e fazer com que Movie e Series herdem dela.
#3.a Crie uma classe TV com os atributois title e year

class TV:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

#3.b Crie uma classe Movie que herda de TV e adicione o atributo rating

class Movie(TV):
    def __init__(self, title, year, rating):
        super().__init__(title, year)
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - Nota: {self.rating}"

#3.c Crie uma classe Serie que herda de TV e adicione o atributo seasons e episodes

class Serie(TV):
    def __init__(self, title, year, seasons, episodes):
        super().__init__(title, year)
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} temporadas, {self.episodes} episódios"

#3.d método __str__ em ambas as classes para formatar a exbição corretamente. Já feito acima.

#4. Criar uma lista de objetos Movie e Series a partir de scraping. Crie uma lista de objetos das classes Movie e Serie a partir do IMDb.
#4.a Uilize o código de Web Scraping do exercício 1 e 2para extrair os títulos, anos e notas dos filmes e para cada filme extraído. 
#4.b Para cada filme extraído, crie um objeto Movie e adicione a uma lista.

filmes = [Movie(titulo, ano, nota) for titulo, ano, nota in movies]

#4.c Criar 2 objetos Series manualmente

series = [Serie("Breaking Bad", 2008, 5, 62), Serie("Lost", 2004, 6, 121)]

#4.d Exibir todos os objetos formatados corretamente

print("\nFilmes:")
for filme in filmes:
    print(filme)

print("\nSéries:")
for serie in series:
    print(serie)

#5a. Criar conexão com o banco SQLite chamado imdb.db

pasta = os.path.dirname(os.path.abspath(__file__)) # Caminho do arquivo atual
db_path = os.path.join(pasta, "imdb.db") # Caminho do banco de dados
DATABASE_URL = f"sqlite:///{db_path}" # URL de conexão com o banco

engine = create_engine(DATABASE_URL, echo=True) 
Base = declarative_base()

# 5.b Criando a tabela de filmes
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

# 5.c Criando a tabela de séries
class Serie(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    seasons = Column(Integer, nullable=False)
    episodes = Column(Integer, nullable=False)

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão para manipular o banco
Session = sessionmaker(bind=engine)
session = Session()

# Fazendo novamente o scraping do site para inserir no banco pois irei converter os anos para int e notas para float e fazer um tratamento de erros diferente do que fiz acima, usando o N/A.

# Encontrando a lista de filmes (fazendo novamente para inserir no banco)
filmes = soup.select('li.ipc-metadata-list-summary-item')

# 5.d Processar os dados e inserir no banco
for i, filme in enumerate(filmes, start=1):
    titulo_elem = filme.find('h3')
    titulo = titulo_elem.text.strip() if titulo_elem else "N/A"

    # Remover número do ranking antes do título
    titulo = titulo[3:] if i < 10 else titulo[4:]

    ano_elem = filme.select_one('.cli-title-metadata-item')
    ano = int(ano_elem.text.strip()) if ano_elem else 0

    nota_elem = filme.select_one('.ipc-rating-star--rating')
    nota = float(nota_elem.text.strip()) if nota_elem else 0.0

    # Criando objeto Movie para podermos fazer a inserção no banco usando try/except (5e)
    novo_filme = Movie(title=titulo, year=ano, rating=nota)

    try:
        session.add(novo_filme)
        session.commit()
        print(f"Filme adicionado: {titulo} ({ano}) - Nota: {nota}")
    except:
        session.rollback()
        print(f"Filme já existe: {titulo}")

# Criar manualmente algumas séries (feito novamente para inserir no banco) (5d)
series = [
    Serie(title="Breaking Bad", year=2008, seasons=5, episodes=62),
    Serie(title="Lost", year=2004, seasons=6, episodes=121),
]

# Inserir as séries no banco - utilizar o try/except já nos ajuda a evitar inserir séries duplicadas, como por exemplo quando rodarmos o código mais de uma vez.

for serie in series: #5e
    try:
        session.add(serie)
        session.commit()
        print(f"Série adicionada: {serie.title} ({serie.year}) - {serie.seasons} temporadas")
    except:
        session.rollback()
        print(f"Série já existe: {serie.title}")

# Fechar sessão
session.close()
print("\nBanco de dados atualizado com sucesso!")

#Extra: Consulta no banco e exibição dos resultados

filmes = session.query(Movie).all()

print("\nFilmes no banco:")
for filme in filmes:
    print(f"{filme.title} ({filme.year}) - Nota: {filme.rating}")

#######################################################

# 6. Consultar os dados do banco com Pandas    

# Caminho do banco de dados
pasta = os.path.dirname(os.path.abspath(__file__)) # Fazendo novamente para pegar o caminho correto
caminho_banco = os.path.join(pasta, "imdb.db") # Caminho do banco de dados


try: #Usando o try/except para evitar erros de conexão (6d)
    # Conectando ao banco de dados
    conn = sqlite3.connect(caminho_banco)
    
    # Ler todas as linhas da tabela movies (6a)
    movies_df = pd.read_sql("SELECT * FROM movies", conn)
    
    # Ler todas as linhas da tabela series (6b)
    series_df = pd.read_sql("SELECT * FROM series", conn)
    
    # Exibir as 5 primeiras linhas de cada tabela (6c)
    print("\nPrimeiros 5 filmes:") 
    print(movies_df.head().to_string(index=False)) # index=False para não exibir o índice
    
    print("\nPrimeiras 5 séries:")
    print(series_df.head().to_string(index=False)) # index=False para não exibir o índice
    
    # 7. Análise de Dados com Pandas

    print("\nOrdene os filmes pelo rating, do maior para o menor:") #(7a)
    movies_df = movies_df.sort_values(by="rating", ascending=False)
    print(movies_df.to_string(index=False)) # index=False para não exibir o índice
     
    print("\nTop 5 filmes mais bem avaliados:") #(7c)
    top_movies = movies_df.sort_values(by="rating", ascending=False)
    print(top_movies.head(5).to_string(index=False)) # index=False para não exibir o índice

    print("\nFilmes com rating acima de 9.0:") #(7b)
    high_rating_movies = top_movies[top_movies["rating"] > 9.0]
    print(high_rating_movies.to_string(index=False)) # index=False para não exibir o índice

    # 8. Exportando os dados para CSV e JSON
    movies_csv = os.path.join(pasta, "movies.csv")
    movies_json = os.path.join(pasta, "movies.json")
    series_csv = os.path.join(pasta, "series.csv")
    series_json = os.path.join(pasta, "series.json")
    
    try: #Usando o try/except para evitar erros de exportação (8.c)

        #8.a Salvando os dados de filmes e séries em movies.csv e series.csv
        #8.b Salvando os dados de filmes e séries em movies.json e series.json

        movies_df.to_csv(movies_csv, index=False)
        movies_df.to_json(movies_json, orient="records", indent=4)
        series_df.to_csv(series_csv, index=False)
        series_df.to_json(series_json, orient="records", indent=4)
        print("\nDados exportados com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar os dados: {e}")
    
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    
finally:
    # Fechar conexão
    conn.close()
    print("\nConexão com o banco de dados fechada! Obrigado por usar o AT do André L M Ferreira")


