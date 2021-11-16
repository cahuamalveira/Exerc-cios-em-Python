#https://youtu.be/cwrqIztaAwk
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogador = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogador4': randint(1, 6),}
ranking = list()
print('Valores Sorteados: ')
for k, v in jogador.items():
    print(f'{k} tirou {v}')
    sleep(0.2)
print('*********PODIUM*********')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')
    sleep(0.5)





