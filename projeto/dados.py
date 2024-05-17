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
    'will bank': 'https://bancodata.com.br/relatorio/willbank/',
    'xp inc' : 'https://bancodata.com.br/relatorio/xp-investimentos-cctvm-sa/'
}

def excluir(z):
    for index, value in enumerate(z):
        z[index] = z[index].replace("\n", "")

Bruto_site_nomes = requests.get('https://www.infomoney.com.br/cotacoes/empresas-b3/')
site_nomes = BeautifulSoup(Bruto_site_nomes.content,'html.parser')
banco_nome = site_nomes.find_all('td',{'class': 'higher'})
nome = [banco_nome[i].text for i in range(len(banco_nome))]

x = requests.get('https://www.infomoney.com.br/cotacoes/empresas-b3/')
y = BeautifulSoup(x.content,'html.parser')
u = y.find_all('td',{'class':'strong'})
v = [u[i].text.lower() for i in range(len(u))]

excluir(nome)
excluir(v)

nomes_bolsa = {}
for i,j in zip(nome, v):
    nomes_bolsa[i] = j

def saida(banco,dd):
    forma = input('Deseja extrair esse arquivo? Se sim, qual dessas formatação:\ntxt,')
    if forma == 'txt':
      with open(f'banco_{banco}.txt','w') as arquivo:
         arquivo.write(f'o banco {banco}\n------------------------------------------------------------------------')
         arquivo.write(f'\nPUBLICAÇÃO: {dd[0]} \nLUCRO LÍQUIDO (R$): {dd[1]} \nPATRIMÔNIO LÍQUIDO (R$): {dd[2]} \nATIVO TOTAL (R$): {dd[3]} \nCAPTAÇÕES (R$): {dd[4]} \nCARTEIRA DE CRÉDITO CLASSIFICADA (R$): {dd[5]} \nPATRIMÔNIO DE REFERÊNCIA RWA (R$): {dd[6]}')
         arquivo.write(f'\nNÚMERO DE AGÊNCIAS: {dd[7]} \nNÚMERO DE PONTOS DE ATENDIMENTO: {dd[8]}')
         arquivo.write('------------------------------------------------------------------------')
print(nomes_bolsa)
