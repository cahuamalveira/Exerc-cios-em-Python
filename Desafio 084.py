#https://youtu.be/zPtvuLiEdKk
#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma
#lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
maior = menor = 0
dado = []
principal = []
while True:
    dado.append(str(input('Digite um nome:').strip()))
    dado.append(float(input('Qual seu peso?')))
    if len(principal) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    principal.append(dado[:])
    dado.clear()
    usuario = str(input('Você deseja continuar?[S/N]'))
    if usuario in 'NnNãonaonãoNAO':
        break
print(f'Foram cadastradas {len(principal)} pessoas')
for u in principal:
    print(f'{u[0]} pesa {u[1]} quilos.')
print(f'O maior peso foi: {maior}')
print(f'E o menor peso foi: {menor}')
