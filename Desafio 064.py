#https://www.youtube.com/watch?v=mYlbttiLHM0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=65
#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número:[999 para parar]'.strip()))
    print('Número incorreto, tente novamente!'.strip())
    cont = cont + 1
    soma = n + soma
print (f'A soma de todos os {cont - 1} números foi de: {soma - 999}!')