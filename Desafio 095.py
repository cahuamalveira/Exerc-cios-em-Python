#https://youtu.be/mw1So0r317Y
#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
busca = list()
times = list()
partidas = list()
gols = 0
while True:
    jogador.clear()
    jogador['nome'] = (str(input('Qual o nome do Jogador?')))
    #partidas.append(jogador['nome'])
    tot = int(input(f'De quantas partidas {jogador["nome"]} participou?'))
    partidas.clear()
    for g in range(0, tot):
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez no jogo {g + 1}?')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        usuario = str(input('Deseja continuar?(S/N)'.strip().upper()))
        if usuario in 'SN':
            break
        print('Não entendi, digite novamente por favor!')
    if usuario in 'N':
        break
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(times):
    print(f' {k+1}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print('')
while True:
    busca = int(input(f'Deseja buscar os dados de qual jogador? (999 PARA PARAR)'))
    busca = busca - 1
    if busca == 999:
        break
    if busca >= len(times):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {times[busca]["nome"]}:')
        for i, g in enumerate(times[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('='*40)
print('Volte sempre')