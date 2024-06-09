from bs4 import BeautifulSoup
import requests, json, textwrap
from dados import url,nome_na_bolsa,chave_brapi
import yfinance 
from time import localtime, strftime
from deep_translator import GoogleTranslator



def excluir(z):
    for index, value in enumerate(z):
        z[index] = z[index].replace("\n", "")

def saida(banco,dd):
    forma = input('Deseja extrair esse arquivo? Se sim, qual dessas formatação:\ntxt,')
    if forma == 'txt':
      with open(f'banco_{banco}.txt','w') as arquivo:
         arquivo.write(f'o banco {banco}\n------------------------------------------------------------------------')
         arquivo.write(f'\nPUBLICAÇÃO: {dd[0]} \nLUCRO LÍQUIDO (R$): {dd[1]} \nPATRIMÔNIO LÍQUIDO (R$): {dd[2]} \nATIVO TOTAL (R$): {dd[3]} \nCAPTAÇÕES (R$): {dd[4]} \nCARTEIRA DE CRÉDITO CLASSIFICADA (R$): {dd[5]} \nPATRIMÔNIO DE REFERÊNCIA RWA (R$): {dd[6]}')
         arquivo.write(f'\nNÚMERO DE AGÊNCIAS: {dd[7]} \nNÚMERO DE PONTOS DE ATENDIMENTO: {dd[8]}')
         arquivo.write('------------------------------------------------------------------------')


def site(banco):
  if banco in url:
      url_banco = url[banco]
  else:     
    url_banco = f"https://www.bancodata.com.br/relatorio/{banco}/"
  pagina = requests.get(url_banco)
  site = BeautifulSoup(pagina.content, 'html.parser')
  publicacao = site.find_all('div', attrs={'class': 'main-info'})
  dd = [i.find('strong').text for i in publicacao]
  excluir(dd)
  print('----------------------------\n')
  print(f'PUBLICAÇÃO: {dd[0]} \nLUCRO LÍQUIDO (R$): {dd[1]} \nPATRIMÔNIO LÍQUIDO (R$): {dd[2]} \nATIVO TOTAL (R$): {dd[3]} \nCAPTAÇÕES (R$): {dd[4]} \nCARTEIRA DE CRÉDITO CLASSIFICADA (R$): {dd[5]} \nPATRIMÔNIO DE REFERÊNCIA RWA (R$): {dd[6]}')
  print(f'NÚMERO DE AGÊNCIAS: {dd[7]} \nNÚMERO DE PONTOS DE ATENDIMENTO: {dd[8]}')
  



def investimentos(banco):
      bolsa = nome_na_bolsa[banco].lower()
      api = f'https://brapi.dev/api/quote/{bolsa}?range=5d&interval=1d&modules=summaryProfile&token={chave_brapi}'
      dados = requests.get(api).json()
      print("preço: R$ ", dados['results'][0]['regularMarketPrice'])
      print("o maior preço do dia: R$", dados['results'][0]['regularMarketDayHigh'])
      print("o menor valor do dia: R$", dados['results'][0]['regularMarketDayLow'])
      print("numero total de ações: ", dados['results'][0]['regularMarketVolume'])
      print('----------------------------\n')
      print("nome: ", dados['results'][0]['longName'])
      print("símbolo: ", dados['results'][0]['symbol'])
      print('endereço: ',dados['results'][0]['summaryProfile']['address1'],';',dados['results'][0]['summaryProfile']['address2'])
      print(f"Localizado: {dados['results'][0]['summaryProfile']['city']}, {dados['results'][0]['summaryProfile']['state']}, {dados['results'][0]['summaryProfile']['country']}")
      if banco == 'b3':
          print('telefone: 4200 0277')
      else:
          print('telefone: ',dados['results'][0]['summaryProfile']['phone'])
      print('site: ',dados['results'][0]['summaryProfile']['website'])

      tradutor = GoogleTranslator(source= "en", target= "pt")
      texto = dados['results'][0]['summaryProfile']['longBusinessSummary']
      traducao = tradutor.translate(texto)
      texto = textwrap.fill(traducao, width=80)
      print('--------------HISTORIA-------------\n')
      print(texto)
