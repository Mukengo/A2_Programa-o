import requests
from bs4 import BeautifulSoup
import time

def raspar_varias_paginas_g1(paginas=5):
    base_url = "https://g1.globo.com/ultimas-noticias/"
    noticias = []

    for pagina in range(1, paginas + 1):
        print(f"Raspando página {pagina}...")
        url = f"{base_url}index/feed/pagina-{pagina}.ghtml"
        resposta = requests.get(url)

        if resposta.status_code != 200:
            print(f"Erro ao acessar página {pagina}")
            continue

        sopa = BeautifulSoup(resposta.text, 'html.parser')
        titulos = sopa.find_all('a', class_='feed-post-link')

        for titulo in titulos:
            texto = titulo.get_text(strip=True)
            if texto not in noticias:
                noticias.append(texto)

        time.sleep(1)

    return noticias

def salvar_em_txt(lista_noticias, nome_arquivo="noticias_g1.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for noticia in lista_noticias:
            arquivo.write(noticia + "\n")
    print(f"\n✅ Arquivo '{nome_arquivo}' salvo com {len(lista_noticias)} notícias.")

if __name__ == "__main__":
    noticias_g1 = raspar_varias_paginas_g1(paginas=10)  # Pode mudar o número de páginas aqui
    salvar_em_txt(noticias_g1)
