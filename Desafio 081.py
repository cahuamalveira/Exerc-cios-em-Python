#https://www.youtube.com/watch?v=SXJKAVVlvGA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=82
#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    n = int(input('Digite um número:').strip())
    lista.append(n)
    usuario = input('Você deseja continuar?[S/N]'.strip())
    if usuario in 'NnNãonãoNAOnao':
        print('Obrigado por participar.')
        break
print(f'Foram digitados {len(lista)} números.')
print (sorted(lista, reverse=True))
if 5 in lista:
    print ('Você digitou o número 5 e ele está na sua lista.')
else:
    print ('Você não digitou o número 5.')

