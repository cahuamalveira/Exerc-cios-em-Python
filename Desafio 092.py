#https://youtu.be/Vsqemzdrj78
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome:'))
dados['Ano de Nascimento'] = int(input('Ano de nascimento:'))
dados['Idade'] = [datetime.now().year - dados['Ano de Nascimento']]
del dados['Ano de Nascimento']
dados['Carteira de trabalho'] = int(input('Carteira de trabalho: (0 caso não tenha)'))
if dados['Carteira de trabalho'] != 0:
        dados['Ano de contratação'] = int(input('Ano de contratação:'.strip()))
        dados['Salário'] = float(input('Salário:'))
        dados['Aposentadoria'] = {dados['Ano de contratação'] + 35}
for v, k in dados.items():
        print(f'{v} tem o valor {k}')

#print(dados)
#print(datetime.now().year)