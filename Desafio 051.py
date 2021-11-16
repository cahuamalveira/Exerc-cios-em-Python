pt = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimo = pt + (10) * razao
for c in range (pt, decimo, razao):
    print (f'{c}', end=' - ')