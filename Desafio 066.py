#https://www.youtube.com/watch?v=d2ug6quC1bk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=67
#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

#n = 0
#cont = 0
#soma = 0
#while n != 999:
   # n = int(input('Digite um número: [999 para parar]'.strip()))
    #cont += 1
    #soma += n
#print (f'Você digitou {cont - 1} números e a soma entre eles é: {soma - 999}')

#Jeito do guanabara \/

soma = cont = 0
while True:
    n = int(input('Digite um número: [999 para parar]'.strip()))
    if n == 999:
        break
    soma += n
    cont += 1
print (f'A soma entre os {cont} números digitados foi de:{soma}')



