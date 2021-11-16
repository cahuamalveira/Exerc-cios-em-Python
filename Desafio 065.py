#https://www.youtube.com/watch?v=QNPuPlPM--0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=66
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
media  = soma = cont = n = maior = menor = 0
repeat = 'Sim'
while repeat == 'Sim':
    n = int(input('Digite um valor:'.strip()))
    repeat = str(input('Você deseja continuar digitando valores?[Sim/Não]'.strip()))
    cont = cont + 1
    soma = n + soma
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print (f'A soma entre todos os números digitados foi de:{soma}')
print (f'Foram mostrados {cont} números e a média entre eles é de: {media}')
print(f'O Maior número foi: {maior}')
print (f'O menor número foi: {menor}')
