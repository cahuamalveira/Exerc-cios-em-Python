soma = 0
cont = 0
for a in range (1, 501, 2):
    if a % 3 == 0:
        soma = soma + a
        cont = cont + 1
print (f'Bom... Então é isso né familia, o resultado da soma dos {cont} números encontrados é de: {soma}')