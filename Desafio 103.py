def ficha(jogador = 'desconhecido', gol=0):
    print(f'O jogador {jogador} marcou {gol} gols')


n1 = str(input('Qual o nome do jogador?'))
n2 = str(input('Quantos gols ele marcou?'))
if n2.isnumeric():
    n2 =int(n2)
else:
    n2 = 0
if n1.strip() == '':
    ficha(gol=n2)
else:
    ficha(n1, n2)