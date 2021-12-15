"""https://youtu.be/vp9UX7wr92o
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros (números) com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep
from random import randint

def maior(*n):
    print('Vamos analisar os números repassados!')
    for valor in n:
        sleep(0.3)
        print(f'{valor}', end=' ')
    print('')
    print(f'O valor máximo entre esses valores é: {max(n)} e o menor valor foi: {min(n)}')
    print(f'Foram analisados {len(n)} números')
    print('=*' * 50)


maior(1, 7, 9, 4, 5)
maior(4, 17, 6)
maior(0, -9, -3)
maior(145, 573, 313, 913, 9, 419)





#Lógica que eu segui pra fixar como se usa def/pra projetar como eu ia escrever o exercício.
"""n = {randint(0, 100),randint(0, 100), randint(0, 100), randint(0, 100) }
print(f'O maior número de {n} é {max(n)}')"""

