#https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=41
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
print ('=' *30)
print ('{:^30}'.format('BANCO CAIXA'))
print ('='*30)
valor = int(input('Qual valor você quer sacar?'.strip()))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print (f'Total de {totced} cédulas de: R${ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print ('*' * 50)
print ('Volte sempre a CAIXA.')
