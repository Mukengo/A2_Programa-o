import requests
from bs4 import BeautifulSoup

# Lista de seções da CNN para visitar
secoes = [
    'https://www.cnnbrasil.com.br/politica/',
    'https://www.cnnbrasil.com.br/economia/',
    'https://www.cnnbrasil.com.br/nacional/',
    'https://www.cnnbrasil.com.br/internacional/',
    'https://www.cnnbrasil.com.br/entretenimento/',
    'https://www.cnnbrasil.com.br/tecnologia/',
]

titulos = []

for url in secoes:
    print(f'Raspando: {url}')
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # CNN geralmente usa h2 e h3 nas listagens
        for tag in soup.find_all(['h2', 'h3']):
            texto = tag.get_text(strip=True)
            if texto and len(texto) > 30:
                titulos.append(texto)
    else:
        print(f'Erro ao acessar: {url} — Código {response.status_code}')

# Remove duplicatas
titulos = list(set(titulos))

# Salva no arquivo
with open('noticias_cnn.txt', 'w', encoding='utf-8') as f:
    for titulo in titulos:
        f.write(titulo + '\n')

print(f'{len(titulos)} títulos salvos em "noticias_cnn.txt".')
