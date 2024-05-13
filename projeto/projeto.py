from bs4 import BeautifulSoup
import requests, json
from pprint import pprint
pprint = print
print = pprint
url = {
    'banco do brasil': 'https://bancodata.com.br/relatorio/bb/',
    'easynvest': 'https://bancodata.com.br/relatorio/easynvest-titulo-cv-sa/',
    'intermedium': 'https://bancodata.com.br/relatorio/intermedium/',
    'paypal': 'https://www.bancodata.com.br/relatorio/10878448/',
    'will bank': 'https://bancodata.com.br/relatorio/willbank/'
}

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
  def monitoria(banco):
     ou = requests.get('https://olinda.bcb.gov.br/olinda/servico/Informes_Ouvidorias/versao/v1/odata/Ouvidorias?$top=1000&$skip=0&$format=json&$select=Nome,WebSite,Telefone').json()

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
  