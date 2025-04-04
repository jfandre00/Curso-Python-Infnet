episodios_elem = serie.find_all('span', class_='cli-title-metadata-item')
    if len(episodios_elem) > 1:
        episodios_text = episodios_elem[1].text.replace(' eps', '').strip()
        episodios = episodios_text if episodios_text else "N/A"
    else:
        episodios = "N/A"