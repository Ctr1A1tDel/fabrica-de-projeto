from bs4 import BeautifulSoup
import requests, json
from defs import excluir,saida,site,investimentos
from dados import url,nome_na_bolsa
import yfinance 

try:
  loop = 'sim'
  while True:
    if loop == 'sim' or loop == 's':
      banco = input('banco: ').lower().replace(' ','-')
      
      site(banco)
      investimentos(banco)
      loop = input('\nmais alguma coisa? ')
    else:
      break
      
  else:
    print('obrigado por usar')

except IndexError:
  print('digite o nome certo')
  