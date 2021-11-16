n1 = int(input('Digite um valor entre 0 e 10:'.strip()))
n2 = int(input('Digite um valor entre 0 e 10:'.strip()))
n3 = int(input('Digite um valor entre 0 e 10:'.strip()))
n4 = int(input('Digite um valor entre 0 e 10:'.strip()))
tupla = (n1, n2, n3, n4)
#tres = (tupla.index(3)+1)
print (f'O número 9 aparece exatas {tupla.count(9)} vezes')
if 3 in tupla:
    tres = (tupla.index(3) + 1)
    print (f'O valor 3 foi digitado na {tres} posição.')
else:
    print ('O número 3 não foi digitado hora nenhuma.')
print (f'Os números pares encontrados foram:',end='')
for n in tupla:
    if n % 2 == 0:
        print (n, end=', ')

