import requests, json
from time import localtime, strftime
from pprint import pprint
print == pprint
pprint == print
from key_Alpha import chave

#cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#cotacoes = cotacoes.json()
#cotacoes_dolar = cotacoes['BTCBRL'] ['bid']
##pprint(cotacoes)
#print(cotacoes_dolar)
#banco = input()
ou = requests.get('https://olinda.bcb.gov.br/olinda/servico/Informes_Ouvidorias/versao/v1/odata/Ouvidorias?$top=1000&$skip=0&$format=json&$select=Nome,WebSite,Telefone').json()

#url = {
#    'banco do brasil': 'https://bancodata.com.br/relatorio/bb/',
#    'easynvest': 'https://bancodata.com.br/relatorio/easynvest-titulo-cv-sa/',
#    'intermedium': 'https://bancodata.com.br/relatorio/intermedium/',
#    'paypal': 'https://www.bancodata.com.br/relatorio/10878448/',
#    'will bank': 'https://bancodata.com.br/relatorio/willbank/'
#}
#
#while True:
#    banco = input() 
#    nome =ou['value'][0]['Nome'].split()
#    if banco == nome[0]:
#        print('cu')
#        break
#    else:
#        print('bu')
#        break

#data = strftime("%Y%m", localtime())


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave}'

r = requests.get(url)
data = r.json()

print(data)


