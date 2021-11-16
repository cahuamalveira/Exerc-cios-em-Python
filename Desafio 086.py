#https://youtu.be/EGmlFdwD4C4
#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0,3):
    for b in range(0,3):
        matriz[c][b] = int(input(f'Digite um número para [{c},{b}]:'))
for c in range(0,3):
    for b in range(0,3):
        print(f'[{matriz[c][b]}]', end='')
    print()