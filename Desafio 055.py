#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#https://youtu.be/Kjpb_IAOKRQ
maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input(f'Qual o peso da pessoa {p}?'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'O maior peso lido foi de {maior}Kg.')
print (f'O menor peso lido foi de {menor}Kg.')


print ('')