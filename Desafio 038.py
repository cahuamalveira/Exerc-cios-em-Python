n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    print (f'O número {n1} é o maior número dentre os que você digitou')
elif n2 > n1:
    print (f'O número {n2} é o maior número dentre os que você digitou')
elif n1 == n2:
    print ('Ambos os números são iguais')