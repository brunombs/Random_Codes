from bs4 import BeautifulSoup
import requests
import json

def json_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    data_json = soup.find(id='initial-data').get('data-json')
    return json.loads(data_json)

def mostra_dados_do_anuncio(url):
    data = json_from_url(url)
    descricao = data['ad']['body']
    phone =  data['ad']['phone']['phone']
    user = data['ad']['user']['name']
    preco = data['ad']['price']
    print('Vendedor=',user)
    print('Telefone=',phone)
    print('Descrição=',descricao)
    print('preco=',preco)


url_eletronicos='https://www.olx.com.br/computadores-e-acessorios/notebook-e-netbook?q=macbook%20pro&sf=1'
data = json_from_url(url_eletronicos)

adList = data['listingProps']['adList']
for anuncio in adList:
    subject = anuncio.get('subject')
    if subject:
        print('------------------------')
        descricao = anuncio.get('subject')
        url = anuncio.get('url')
        print('Descricao do produto:',descricao)
        print('URL do produto=',url)
        mostra_dados_do_anuncio(url)