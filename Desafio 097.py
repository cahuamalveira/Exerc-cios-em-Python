#https://youtu.be/Q6basnSo7r0
#Faça um programa que tenha uma função chamada escreva(),
#que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

while True:
    def escreva(txt):
        t = len(txt) + 4
        print('*' * t)
        print(f' {txt}')
        print('*' * t)


    escreva(str(input('Escreva alguma mensagem:')))
    usuario = str(input('Caso queira parar, escreva o número: 999 '
                        'Caso queira continuar, digite qualquer número de 0 a 998'))
    if usuario == '999':
        print('Obrigado por participar')
        break