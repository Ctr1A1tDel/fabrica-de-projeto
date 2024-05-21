from bs4 import BeautifulSoup
import requests, json
from dados import url,nome_na_bolsa
import yfinance 
from time import localtime, strftime


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
  print('----------------------------\n')
  saida(banco,dd)

def investimentos(banco):
  
  if banco in nome_na_bolsa:
    bolsa = nome_na_bolsa[banco]
    tiket = yfinance.Ticker(f'{banco}.SA')
    print(tiket)
  else:
    print('n achei')
    
