#https://youtu.be/5yKiud-YNaE
#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
#partida. No final, tudo isso será guardado em um dicionário.
jogador = {}
partidas = []
gols = 0
jogador['nome'] = str(input('Qual o nome do Jogador?'))
tot = int(input(f'Quantas partidas {jogador["nome"]} participou?'))
for g in range(0, tot):
    partidas.append(int(input(f'Quantos gols esse jogador fez no jogo {g + 1}?')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print(jogador)
for v, k in jogador.items():
    print(f'O campo {v} tem valor {k}')
print('_=_'*25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c, n in enumerate(jogador['gols']):
    print(f'Na partida {c + 1} o jogador {jogador["nome"]} fez {n} gols')
#Não faz sentido fazer tudo em uma lista pra depois jogar tudo pra um dicionário.
