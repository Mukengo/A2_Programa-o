import requests
from bs4 import BeautifulSoup

# Seções da Folha para raspar
secoes = [
    'https://www.folha.uol.com.br/poder/',
    'https://www.folha.uol.com.br/equilibrioesaude/',
    'https://www.folha.uol.com.br/economia/',
    'https://www.folha.uol.com.br/mundo/',
    'https://www.folha.uol.com.br/cotidiano/',
    'https://www.folha.uol.com.br/ilustrada/',
]

titulos = []

for url in secoes:
    print(f'Raspando: {url}')
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Na Folha, títulos ficam em <h2> com classe 'c-headline__title'
        for h2 in soup.find_all('h2', class_='c-headline__title'):
            texto = h2.get_text(strip=True)
            if texto and len(texto) > 30:
                titulos.append(texto)
    else:
        print(f'Erro ao acessar: {url} — Código {response.status_code}')

# Remove duplicatas
titulos = list(set(titulos))

# Salva em arquivo
with open('noticias_folha.txt', 'w', encoding='utf-8') as f:
    for titulo in titulos:
        f.write(titulo + '\n')

print(f'{len(titulos)} títulos salvos em "noticias_folha.txt".')
