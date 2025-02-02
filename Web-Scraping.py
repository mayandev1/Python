# instale as bibliotecas no terminal:
# requests = pip install requests
# bs4 = pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def url_valida(url):
    try:
        resultado = urlparse(url)
        return all([resultado.scheme, resultado.netloc])
    except ValueError:
        return False

def web_scraping(url, elemento_titulo="h1", elemento_paragrafo="p"):
    if not url_valida(url):
        print("URL inválida. Por favor, insira um URL válido.")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na solicitação
    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    # Extração de informações personalizadas
    titulo = soup.find(elemento_titulo).text if soup.find(elemento_titulo) else "Título não encontrado"
    paragrafos = soup.find_all(elemento_paragrafo)

    print("Título:", titulo)
    print("Parágrafos:")
    for paragrafo in paragrafos:
        print("-", paragrafo.text)

if __name__ == "__main__":
    url = input("Insira o URL da página: ")
    elemento_titulo = input("Insira o elemento HTML para o título (padrão: h1): ") or "h1"
    elemento_paragrafo = input("Insira o elemento HTML para os parágrafos (padrão: p): ") or "p"
    web_scraping(url, elemento_titulo, elemento_paragrafo)
