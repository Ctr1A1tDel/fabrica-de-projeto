import requests, json
from time import localtime, time
from pprint import pprint
import pandas_datareader as pdr
from key_Alpha import chave_alpha,chave_brapi
print == pprint
pprint == print
#cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#cotacoes = cotacoes.json()
#cotacoes_dolar = cotacoes['BTCBRL'] ['bid']
##pprint(cotacoes)
#print(cotacoes_dolar)
#banco = input()
#ou = requests.get('https://olinda.bcb.gov.br/olinda/servico/Informes_Ouvidorias/versao/v1/odata/Ouvidorias?$top=1000&$skip=0&$format=json&$select=Nome,WebSite,Telefone').json()

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
#url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=ROXO34.SA&apikey={chave}'
#url = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo'

#r = requests.get(url)
#data = r.json()

#$pprint(data['Weekly Adjusted Time Series']['2024-05-20'])


#pprint(data)

#data_inical = '2024-04-01'
#data_final = str(localtime())
#tabela_cotacao =pdr.get_data_yahoo('BBAS3.SA',data_inical,data_final)
#display(tabela_cotacao)
nome_na_bolsa={
    'b3':	'B3SA3',
    'banco do brasil':	'BBAS3',
    'bradesco':	'BBDC4',
    'itau':	'ITUB4',
    'banco do brasil':'	BBAS3',
}


banco = input('banco: ').lower()
if banco in nome_na_bolsa:
    bolsa = nome_na_bolsa[banco].lower()
    api = f'https://brapi.dev/api/quote/{bolsa}?range=5d&interval=1d&modules=summaryProfile&token={chave_brapi}'
    dados = requests.get(api).json()
    pprint(dados)
else:
    print('cu')