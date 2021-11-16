#https://youtu.be/Hd7Ycaj61xE
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.
from random import randint
import time
cont = 0
tot = 0
sorteio = []
jogos = []
vezes = int(input('Quantas jogos você quer?').strip())
tot = 1
while tot <= vezes:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    sorteio.append(jogos[:])
    jogos.clear()
    tot += 1
for c, l in enumerate(sorteio):
    time.sleep(0.5)
    print(f'Jogo {c+1}: {l}')
print ('-------------BOA SORTE-------------')

