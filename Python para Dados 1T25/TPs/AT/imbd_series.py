import requests
from bs4 import BeautifulSoup
import urllib.request

site = "https://www.imdb.com/chart/toptv/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

series = soup.select('li.ipc-metadata-list-summary-item')
series_list = []

for i, serie in enumerate(series, start=1):
    # Título do filme
    titulo_elem = serie.find('h3')
    titulo = titulo_elem.text.strip() if titulo_elem else "N/A"
    
    # Remover o número do ranking antes do título
    titulo_parts = titulo.split('.', 1)
    if len(titulo_parts) > 1:
        titulo = titulo_parts[1].strip()
    
    # Extrair informações de ano
    metadata_items = serie.find_all('span', class_='cli-title-metadata-item')
    ano_info = metadata_items[0].text.strip() if metadata_items else "N/A"
    
    # Tratar o ano (pode ser "2008–2013" ou apenas "2008")
    # Primeiro substituir qualquer tipo de hífen/dash por um hífen comum
    ano_info = ano_info.replace('–', '-').replace('—', '-')
    
    if '-' in ano_info:
        anos = ano_info.split('-')
        ano_inicial = anos[0].strip()
        # Se não tiver ano final (ex: "2008-"), considera como 2025
        ano_final = anos[1].strip() if len(anos) > 1 and anos[1].strip() else "2025"
        temporadas = int(ano_final) - int(ano_inicial) + 1
    else:
        ano_inicial = ano_info.strip()
        ano_final = ano_inicial  # Para séries com apenas um ano
        temporadas = 1  # Assume que tem pelo menos 1 temporada
    
    # Extrair número de episódios
    episodios = "N/A"
    if len(metadata_items) > 1:
        episodios_text = metadata_items[1].text.replace(' eps', '').strip()
        if episodios_text.isdigit():
            episodios = int(episodios_text)
    
    # Adicionar os dados à lista de séries
    try:
        series_list.append((titulo, int(ano_inicial), temporadas, episodios))
    except ValueError as e:
        print(f"Erro ao processar: {titulo} - Ano: {ano_info}")
        print(f"Detalhes do erro: {e}")
        series_list.append((titulo, "N/A", "N/A", episodios))

# Exibir a lista de séries
for serie in series_list:
    print(serie)