import requests,json,pprint
import pandas as pd

requisicao = requests.get('https://olinda.bcb.gov.br/olinda/servico/Informes_Ouvidorias/versao/v1/odata/Ouvidorias?$top=100&$skip=0&$format=json&$select=Nome,WebSite,Telefone')
ava = requisicao.json()


tabela = pd.DataFrame(ava["value"])
print(tabela)