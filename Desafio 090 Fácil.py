#https://youtu.be/HipQYUk4koA
#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em
#um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
boletim = dict()
boletim['Nome'] = str(input('Qual seu nome?'.strip()))
boletim['Média'] = float(input(f'Qual sua média {boletim["Nome"]}?'.strip()))
if boletim['Média'] >= 6:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Média'] < 6:
    boletim['Situação'] = 'Recuperação'
else:
    boletim ['Situação'] = 'Reprovado'
#print(boletim)
for a, o in boletim.items():
    print(f'{a} é igual a: {o}')
#if boletim['Média'] >= 6:
    #print('Você foi aprovado!')
#else:
    #print('Tu reprovou bicho')
#******OU*****