# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# https://www.youtube.com/watch?v=-QkOIHJ1Chw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=59
from random import randint
from time import sleep

num = randint(0, 100)
cont = 0
print('Descubra em qual número estou pensando. Vamos começar?')
sleep(0.7)
acertou = False
while not acertou:
    tent = int(input('Qual o número em que estou pensando?'.strip()))
    cont += 1
    if tent > num:
        print ('Chute um número mais baixo.')
    elif tent < num:
        print ('Chute um número mais alto.')
    if tent == num:
        acertou = True
        print(f'Parabéns, você acertou em {cont} palpites')

print('Fim')
