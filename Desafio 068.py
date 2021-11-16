from random import randint
print ('---------VAMOS JOGAR ÍMPAR OU PAR-----')
cont = 0
while True:
    n = int(input('Digite um número:'.strip()))
    num = randint(0, 10)
    jogo = n + num
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Você quer ímpar ou par?'.strip().upper()))
    print(f'Você jogou {n} e o computador {num}, total de {jogo}.')
    print ('DEU PAR' if jogo % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
       if jogo % 2 == 0:
            cont += 1
            print (f'Parabéns,{jogo} é um número par e você ganhou pela {cont} vez')
       else:
            print ('Você perdeu')
            break
    elif escolha == 'I':
        if jogo % 2 == 1:
            cont += 1
            print (f'Parabéns, {jogo} é um número ímpar e você ganhou pela {cont} vez')
        else:
            print ('Você perdeu.')
            break
print ('Você perdeu para a máquina, acabou.')




