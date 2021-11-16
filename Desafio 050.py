soma = 0
cont = 0
for a in range (1,7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print (f' Você informou {cont} números, e a soma entre esses números foi {soma}')