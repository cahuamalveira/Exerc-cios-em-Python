#https://youtu.be/ETnExBCFeps
#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
#todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
pessoas = dict()
galera = list()
cont = 0
pessoas['Idade'] = dict()
soma = media = 0
while True:
    pessoas['Nomes'] = (str(input('Nome:')))
    while True:
        pessoas['Sexo'] = (str(input('Sexo: [M/F]')))
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Digite novamente')
    pessoas['Idade'] = (int(input('Idade:')))
    cont += 1
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        usuario = str(input('Deseja continuar? (S/N)'.strip()))
        if usuario in 'SN':
            break
        print('Responda novamente com S ou N')
    if usuario == 'N':
        break
media = soma / len(pessoas)
print(f'A) O grupo tem {cont} pessoas')
print(f'B) A média de idade do grupo é: {media} anos ')
print(f'C) As mulheres cadastradas foram:', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nomes"]}',end=', ')
print(' ')
print('C) Pessoas que tem a idade acima da média:')
for p in galera:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

