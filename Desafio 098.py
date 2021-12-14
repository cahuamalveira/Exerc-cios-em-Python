"""https://youtu.be/DCBlt_z2UOE
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

#MINHA SOLUÇÃO EM QUE DESENVOLVI SOZINHO.
from time import sleep
def contador(inicio, fim, passo):
    print('*' * 50)
    for num in range(inicio, fim, passo):
        sleep(0)
        print(num, end=' ')
    print('FIM')


contador(1, 11, 1)
contador(10, 0, -2)
print('*' * 50)
print('Agora é sua vez de personalizar a contagem')
n1 = int(input('Início:'))
n2 = int(input('Fim:'))
n3 = int(input('Intervalo:'))
contador(n1, n2, n3)

#SOLUÇÃO DESENVOLVIDA PELO GUANABARA.

"""def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')
contagem(1, 10, 1)
contagem(10, 0, -2)
print('*' * 50)
print('Agora é sua vez de personalizar a contagem')
n1 = int(input('Início:'))
n2 = int(input('Fim:'))
n3 = int(input('Intervalo:'))
contagem(n1, n2, n3)"""



