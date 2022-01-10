"""https://youtu.be/BMKYnZoxy88
Faça um mini-sistema que utilize o Interactive Help do Python.
 O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores."""

#n = input('Digite alguma função para visualizar o manual:')
#help(n.__doc__)

c = ('\033[m',         # 0 sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 verde
     '\033[0;30;43m',  # 3 amarelo
     '\033[0;30;44m',  # 4 azul
     '\033[0;30;45m',  # 5 roxo
     '\033[7;30m'     # 6 branco
    );

def ajuda(com):
    título(f'Acessando o manual de comando \'{com}\'', 4)
    print(c[2], end='')
    help(com)
    print(c[2], end='')

def título (msg, cor = 0):
    tam = len(msg)
    print(c[cor], end='')
    print('*' * tam)
    print(msg)
    print('*' * tam)
    print(c[0], end='')


comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo', 1)