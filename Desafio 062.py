pt = int(input('Digite o primeiro termo:'.strip()))
razao = int(input('Digite a razão:'.strip()))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
     print (f'{termo}', end=' - ')
     termo += razao
     cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'.strip()))
print ('----FIM-----')
print (f'Foram mostrados {total} números')