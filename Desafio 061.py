pt = int(input('Digite o primeiro termo:'.strip()))
razao = int(input('Digite a razão da progressão:'.strip()))
termo = pt
cont = 1
while cont <= 10:
    print (f'{termo}', end=',')
    termo += razao
    cont += 1
    repeat = input('Você quer mostrar mais alguns termos?'.upper())
    if repeat == 'S' or 'N':
        print (f'{pt}')
print (f'----FIM----')

