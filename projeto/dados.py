from bs4 import BeautifulSoup
import requests, json
from pprint import pprint
print = pprint
pprint = print

url = {
    'banco do brasil': 'https://bancodata.com.br/relatorio/bb/',
    'easynvest': 'https://bancodata.com.br/relatorio/easynvest-titulo-cv-sa/',
    'intermedium': 'https://bancodata.com.br/relatorio/intermedium/',
    'paypal': 'https://www.bancodata.com.br/relatorio/10878448/',
    'will bank': 'https://bancodata.com.br/relatorio/willbank/'
}
   
Bruto_site_nomes = requests.get('https://www.infomoney.com.br/cotacoes/empresas-b3/')
site_nomes = BeautifulSoup(Bruto_site_nomes.content,'html.parser')
banco_nome = site_nomes.find_all('td',{'class': 'higher'})
dados = [i.find('higher').text for i in banco_nome]
#bancos = banco_nome.find_all('td', attrs={'class': 'higher'})

#for index, value in enumerate(banco_nome):
 #   banco_nome = banco_nome[index].replace("\n", "")
#for x,y in enumerate(banco_nome):
#    print( banco_nome[x].text)
print(dados)