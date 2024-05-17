from bs4 import BeautifulSoup
import requests, json
from pprint import pprint
from dados import url,nomes_bolsa,excluir,saida
pprint = print
print = pprint


try:
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
    
    if banco in nomes_bolsa:
      bolsa = nomes_bolsa[banco]
      print(bolsa)
    else:
      print('n achei')

  loop = 'sim'
  while True:
    if loop == 'sim' or loop == 's':
      banco = input('banco: ').lower()
      
      site(banco)
      investimentos(banco)
      loop = input('\nmais alguma coisa? ')
    else:
      break
      
  else:
    print('obrigado por usar')

except IndexError:
  print('digite o nome certo')
  