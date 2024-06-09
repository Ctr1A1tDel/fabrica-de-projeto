from bs4 import BeautifulSoup
import requests, json
from defs import excluir,saida,site,investimentos
from dados import url,nome_na_bolsa
import yfinance 
from time import localtime, strftime

try:
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
  