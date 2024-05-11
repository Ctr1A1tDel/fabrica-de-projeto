from bs4 import BeautifulSoup
import requests
from pprint import pprint
pprint = print
print = pprint

try:
  def site(banco):

    if banco == 'banco do brasil':
       banco = 'bb'

    elif banco == 'easynvest':
      banco = 'easynvest-titulo-cv-sa'

    elif banco == 'inter':
      banco = 'intermedium'


    pagina = requests.get(f'https://bancodata.com.br/relatorio/{banco}/')
    site = BeautifulSoup(pagina.content, 'html.parser')
    publicacao = site.find_all('div', attrs={'class': 'main-info'})
    dd = [i.find('strong').text for i in publicacao]

    if banco == 'easynvest-titulo-cv-sa':
      banco = 'easynvest'
    elif banco == 'intermedium':
      banco = 'inter'
    elif banco == 'wilbank':
      banco = 'will bank'


    for index, value in enumerate(dd):
      dd[index] = dd[index].replace("\n", "")
    print('----------------------------\n')
    print(f'PUBLICAÇÃO: {dd[0]} \nLUCRO LÍQUIDO (R$): {dd[1]} \nPATRIMÔNIO LÍQUIDO (R$): {dd[2]} \nATIVO TOTAL (R$): {dd[3]} \nCAPTAÇÕES (R$): {dd[4]} \nCARTEIRA DE CRÉDITO CLASSIFICADA (R$): {dd[5]} \nPATRIMÔNIO DE REFERÊNCIA RWA (R$): {dd[6]}')
    print(f'NÚMERO DE AGÊNCIAS: {dd[7]} \nNÚMERO DE PONTOS DE ATENDIMENTO: {dd[8]}')
    print('----------------------------\n')

    txt = input('Deseja extrair esses dados informados em arquivo txt? ')
    if txt == 'sim' or txt == 's':
      with open(f'banco_{banco}.txt','w') as arquivo:
         arquivo.write(f'o banco {banco}\n-----------------')
         arquivo.write(f'\nPUBLICAÇÃO: {dd[0]} \nLUCRO LÍQUIDO (R$): {dd[1]} \nPATRIMÔNIO LÍQUIDO (R$): {dd[2]} \nATIVO TOTAL (R$): {dd[3]} \nCAPTAÇÕES (R$): {dd[4]} \nCARTEIRA DE CRÉDITO CLASSIFICADA (R$): {dd[5]} \nPATRIMÔNIO DE REFERÊNCIA RWA (R$): {dd[6]}')
         arquivo.write(f'\nNÚMERO DE AGÊNCIAS: {dd[7]} \nNÚMERO DE PONTOS DE ATENDIMENTO: {dd[8]}')
 # def api(x):
    
  loop = 'sim'
  while True:
    if loop == 'sim' or loop == 's':
      banco = input('banco: ').lower()
      site(banco)
      loop = input('\nmais alguma coisa? ')
    else:
      break
      
  else:
    print('obrigado por usar')

except IndexError:
  print('digite o nome certo')
  