n1 = int(input('Digite um número:'))
print ('''Escolha um número que representa para qual forma você quer converter seu número
[1] para binário 
[2] para octagonal
[3] para hexadecimal''')
opçao = int(input('Qual opção você deseja?'))
if opçao == 1:
    print (f'O número {n1} convertido para binário é igual a {bin(n1)}')
elif opçao == 2:
    print (f'O número {n1} convertido para octagonal é igual a {oct(n1)}')
elif opçao == 3:
    print (f'O número {n1} convertido para hexadecimal é igual a {hex(n1)}')