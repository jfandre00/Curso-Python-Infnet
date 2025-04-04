# AT Python para Dados 1T25 - André L M Ferreira


from bs4 import BeautifulSoup
import urllib.request
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd
import sqlite3
import os

'''
Atenção:
Só consegui o retorno de 25 ocorrências na lista. Isso acontece porque o IMDb carrega a lista dos Top 250 filmes dinamicamente via JavaScript, 
e o BeautifulSoup não executa JavaScript, então ele só captura os elementos HTML que já estão na página no momento do carregamento inicial.
'''

# 1. Extrair os filmes do ranking do IMDb
site = "https://www.imdb.com/chart/top/"

# 1.a Acessar a página IMDb top 250
req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

filmes = soup.select('li.ipc-metadata-list-summary-item')

# 1.b Extrair e exibir os 10 primeiros títulos
titulos_ex1b = soup.find_all('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-495ef71a-2 cpvJUg cli-title with-margin')

print("\nTítulos dos 10 primeiros filmes do IMDb Top 250:\n")
for i in range(10):
    print(titulos_ex1b[i].text.strip())

# 2.a Extrair os dados dos filmes
movies = []

for i, filme in enumerate(filmes, start=1):
    # Título do filme
    titulo_elem = filme.find('h3')
    titulo = titulo_elem.text.strip() if titulo_elem else "N/A"

    # Remover o número do ranking
    titulo_parts = titulo.split('.', 1)
    if len(titulo_parts) > 1:
        titulo = titulo_parts[1].strip()

    # Ano do filme
    ano_elem = filme.select_one('.cli-title-metadata-item')
    ano = ano_elem.text.strip() if ano_elem else "N/A"

    # Nota IMDb
    nota_elem = filme.select_one('.ipc-rating-star--rating')
    nota = nota_elem.text.strip() if nota_elem else "N/A"

    movies.append((titulo, ano, nota))

# 2.b Exibir os 5 primeiros filmes formatados
print("\nOs 5 primeiros filmes do IMDb Top 250:\n")
for i, (titulo, ano, nota) in enumerate(movies[:5], start=1):
    print(f"{i}. {titulo} ({ano}) - Nota: {nota}")

# 3. Criar classes TV, Movie e Serie
class TV:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

class Movie(TV):
    def __init__(self, title, year, rating):
        super().__init__(title, year)
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - Nota: {self.rating}"

class Serie(TV):
    def __init__(self, title, year, seasons, episodes):
        super().__init__(title, year)
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} temporadas, {self.episodes} episódios"

# 4. Criar listas de objetos Movie e Serie
filmes_objs = [Movie(titulo, ano, nota) for titulo, ano, nota in movies]

# Extrair séries
site_series = "https://www.imdb.com/chart/toptv/"
req_series = urllib.request.Request(site_series, headers={'User-Agent': 'Mozilla/5.0'})
response_series = urllib.request.urlopen(req_series)
html_series = response_series.read()
soup_series = BeautifulSoup(html_series, 'html.parser')

series = soup_series.select('li.ipc-metadata-list-summary-item')
series_list = []

for i, serie in enumerate(series, start=1):
    titulo_elem = serie.find('h3')
    titulo = titulo_elem.text.strip() if titulo_elem else "N/A"
    
    titulo_parts = titulo.split('.', 1)
    if len(titulo_parts) > 1:
        titulo = titulo_parts[1].strip()
    
    metadata_items = serie.find_all('span', class_='cli-title-metadata-item')
    ano_info = metadata_items[0].text.strip() if metadata_items else "N/A"
    ano_info = ano_info.replace('–', '-').replace('—', '-')

    try:
        if '-' in ano_info:
            anos = ano_info.split('-')
            ano_inicial = anos[0].strip()
            ano_final = anos[1].strip() if len(anos) > 1 and anos[1].strip() else "2025"
            temporadas = int(ano_final) - int(ano_inicial) + 1
        else:
            ano_inicial = ano_info.strip()
            ano_final = ano_inicial
            temporadas = 1
        
        ano_inicial = int(ano_inicial) if str(ano_inicial).isdigit() else 0
    except ValueError as e:
        print(f"Erro ao processar: {titulo} - Ano: {ano_info}")
        ano_inicial = 0
        temporadas = 1
    
    episodios = 0
    if len(metadata_items) > 1:
        episodios_text = metadata_items[1].text.replace(' eps', '').strip()
        episodios = int(episodios_text) if episodios_text.isdigit() else 0
    
    series_list.append((titulo, ano_inicial, temporadas, episodios))

series_objs = [Serie(titulo, ano, temp, ep) for titulo, ano, temp, ep in series_list]
series_objs.append(Serie("24", 2001, 9, 192)) # Adicionando manualmente uma série
series_objs.append(Serie("Lost", 2004, 6, 121)) 

# 5. Criar banco de dados SQLite
pasta = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(pasta, "imdb_final.db")
DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class MovieDB(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

class SerieDB(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    seasons = Column(Integer, nullable=False)
    episodes = Column(Integer, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Inserir filmes
for titulo, ano, nota in movies:
    try:
        nota_float = float(nota) if nota.replace('.', '').isdigit() else 0.0
        ano_int = int(ano) if str(ano).isdigit() else 0
        session.add(MovieDB(title=titulo, year=ano_int, rating=nota_float))
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao inserir {titulo}: {e}")

# Inserir séries
for titulo, ano, temp, ep in series_list:
    try:
        session.add(SerieDB(title=titulo, year=ano, seasons=temp, episodes=ep))
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao inserir {titulo}: {e}")

# 6. Consultar dados com Pandas
try:
    conn = sqlite3.connect(db_path)
    
    # Ler dados
    movies_df = pd.read_sql("SELECT * FROM movies", conn)
    series_df = pd.read_sql("SELECT * FROM series", conn)
    
    # Exibir dados
    print("\nPrimeiros 5 filmes:")
    print(movies_df.head().to_string(index=False))
    
    print("\nPrimeiras 5 séries:")
    print(series_df.head().to_string(index=False))
    
    # 7. Análise de dados
    print("\nFilmes ordenados por rating:")
    print(movies_df.sort_values('rating', ascending=False).to_string(index=False))
    
    print("\nTop 5 filmes:")
    print(movies_df.nlargest(5, 'rating').to_string(index=False))
    
    print("\nFilmes com rating > 9.0:")
    print(movies_df[movies_df['rating'] > 9.0].to_string(index=False))
    
    # 8. Exportar dados
    movies_df.to_csv(os.path.join(pasta, "movies.csv"), index=False)
    movies_df.to_json(os.path.join(pasta, "movies.json"), orient='records', indent=4)
    series_df.to_csv(os.path.join(pasta, "series.csv"), index=False)
    series_df.to_json(os.path.join(pasta, "series.json"), orient='records', indent=4)
    print("\nDados exportados com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
finally:
    conn.close()
    session.close()
    print("\nProcesso concluído!")