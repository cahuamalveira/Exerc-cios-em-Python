#https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=60
#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
n1 = int(input('Digite um valor:'.strip()))
n2 = int(input('Digite outro valor:'.strip()))
usuario = 0
print('[1] para somar esses dois valores.')
print('[2] para multiplicar esses dois valores.')
print('[3] para saber qual valor é maior.')
print('[4] para digitar novos números.')
print('[5] caso queira sair do programa.')
while usuario != 5:
 usuario = int(input('Digite o número da operação que deseja:'.strip()))
 if usuario == 1:
    print (f'A soma entre {n1} + {n2} é: {n1 + n2}')
 elif usuario == 2:
    print (f' A multiplicação entre {n1} x {n2} é: {n1 * n2}')
 elif usuario == 3:
     if n1 > n2:
         maior = n1
     else:
         maior = n2
     print (f'Entre {n1} e {n2}, o maior número é {maior}')
 elif usuario == 4:
     n1 = int(input('Digite um valor:'.strip()))
     n2 = int(input('Digite outro valor:'.strip()))
 elif usuario ==5:
     print ('Muito obrigado pela sua participação!!!!!!!!!!!')




