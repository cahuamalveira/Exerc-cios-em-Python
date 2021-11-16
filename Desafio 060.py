#https://www.youtube.com/watch?v=9dlBZlkvvxY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=61
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
num = int(input('Digite um número:'.strip()))
print (f'A forma fatorial de {num} é: {factorial(num)}')

#forma empiriquitada do Gustavo Guanabara, a de cima fiz sozinho.
from math import factorial
n = int (input('Digite um número:'.strip()))
c = n
f = 1
print (f'Calculando {n}!: ')
while c > 0:
    print (f'{c}', end='')
    print (' X ' if c > 1 else' = ', end ='')
    f *= c
    c -= 1
print (f'{f}')