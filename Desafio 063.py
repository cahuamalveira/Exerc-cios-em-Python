#https://www.youtube.com/watch?v=w7yn1_Mfu0E&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=64
#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
print ('-' * 30)
print ('SEQUÊNCIA DE FIBONACCI')
print ('-' *30)
numero = int(input('Quantos termos você quer mostrar?'.strip()))
t1 = 0
t2 = 1
print ('~~'*15)
print (f'{t1} > {t2}',end=' > ')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(f'{t3}',end=' > ')
    t1 = t2
    t2 = t3
    cont += 1
print ('FIM')