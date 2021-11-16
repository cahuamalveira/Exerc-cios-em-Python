#https://youtu.be/QhS829x6up4
#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = 0
for c in range(0,3):
    for b in range(0,3):
        matriz[c][b] = int(input(f'Digite um número para [{c},{b}]:'))
        if matriz [c][b] % 2 == 0:
            pares += matriz[c][b]
for c in range(0,3):
    for b in range(0,3):
        print(f'[{matriz[c][b]}]', end='')
    print()
for u in range(0, 3):
    soma += matriz[u][2]
print(f'A soma entre os números pares da matriz é de:{pares}')
print(f'A soma entre os valores da terceira coluna é de: {soma}')
print(f'O maior valor na linha 2 foi de: {max(matriz[1])}')
print(matriz[2])

