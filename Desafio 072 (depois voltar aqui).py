#https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=73
#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
import time
from time import sleep
num =  ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
perg = int(input('Digite um número entre 0 e 20:'))
usuario = ''
while True:
    while perg not in range (0,21):
        print ('Ta tudo errado cara, por favor, tente novamente')
        perg = int(input('Digite um número entre 0 e 20:'))
    print (f'Você digitou o número: {num[perg]} ')
    usuario = str(input('Você deseja continuar? [S/N]'.strip()))
    break
    if usuario == 'N' or 'n':
     print ('Você pipocou você é um bananão.')
     #não consegui perguntar se o usuario que continuar executando o programa ou nao.



