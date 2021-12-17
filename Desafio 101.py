#https://youtu.be/czDcimdc3GU
"""Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
from datetime import date
def voto():
    ano = date.today().year - usuario
    print(f'Com {date.today().year - usuario} anos, se tem:', end=' ')
    if 16 <= ano < 18 or ano > 65:
        return print(f'VOTO OPCIONAL.')
    if ano >= 18:
        return print('VOTO OBRIGATÓRIO')
    if ano < 16:
        return print('VOTO NEGADO')
    #return usuario


usuario = int(input('Em que ano você nasceu?'))
voto()