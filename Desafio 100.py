"""https://youtu.be/MEs-41JcuhM
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
from random import randint
from time import sleep
pares = []
soma = 0
aleatório = []
def sorteia(aleatório):
    print('Sorteando 5 valores: ', end='')
    for cont in range(0, 5):
            n = randint(0, 10)
            aleatório.append(n)
            sleep(0.3)
            print(n, end=' ')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores da lista temos: {soma}')


sorteia(aleatório)
somaPar(aleatório)



