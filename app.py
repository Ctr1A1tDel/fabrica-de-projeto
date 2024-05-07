import flet as ft
import requests
from bs4 import BeautifulSoup

def main(page):

    def banco(e):
        if not entrada_nome.value:
            entrada_nome.error_text = 'por favor preencha o seu nome'
            page.update()
        else:
            nome = entrada_nome.value
            pagina = requests.get(f'https://bancodata.com.br/relatorio/{nome}/')
            site = BeautifulSoup(pagina.content, 'html.parser')
            publicacao = site.find_all('div', attrs={'class': 'main-info'})
            dd = [i.find('strong').text for i in publicacao]
            
            for index, value in enumerate(dd):
                dd[index] = dd[index].replace("\n", "")

        page.clean()
        page.add(ft.Text(
                f'PUBLICAÇÃO: {dd[0]} \nLUCRO LÍQUIDO (R$): {dd[1]} \nPATRIMÔNIO LÍQUIDO (R$): {dd[2]} \nATIVO TOTAL (R$): {dd[3]} \nCAPTAÇÕES (R$): {dd[4]} \nCARTEIRA DE CRÉDITO CLASSIFICADA (R$): {dd[5]} \nPATRIMÔNIO DE REFERÊNCIA RWA (R$): {dd[6]}'
                f'NÚMERO DE AGÊNCIAS: {dd[7]} \nNÚMERO DE PONTOS DE ATENDIMENTO: {dd[8]}'

        ),ft.ElevatedButton('mais alguma coisa',on_click=banco)
        )
        

    entrada_nome = ft.TextField(label='digite o seu nome do banco')

    page.add(
        entrada_nome,
        ft.ElevatedButton('clique em mim',on_click=banco)
    )
    pass


ft.app(target=main)

