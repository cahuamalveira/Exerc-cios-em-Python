#https://www.youtube.com/watch?v=RexybLcGewA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=74
#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
times = ('Palmeiras', 'Atlético MG', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athlético Paranaense', 'Ceará', 'Peixe',
         'Atlético Goianiense', 'Bahia', 'Curintcha', 'Flusão', 'Juventude', 'Internacional', 'Sport', 'Cuiabá',
         'São Paulo', 'América MG','Grêmio', 'Chapecoense')
print (f'Lista de times do brasileirão: {times}')
print (f'\033[32m','---'*8, 'ZONA DE CLASSIFICAÇÃO PRA LIBERTADORES', '---' *8)
for cont in range (0, len(times[0:5])):
    print ('\033[32m'f'{cont + 1}º: {times[cont]}')
print ('\033[1;31m','---'*8, 'ZONA DE REBAIXAMENTO', '---' *8)
for pos, t in enumerate(times[len(times)-4:]):
            print(f'\033[1;31m{len(times)- 3 + pos}º {t}')
#Não entendi essa parte da zona de rebaixamento direito

print ('\033[34m''---'*30)
print ('\033[34m'f'Os integrantes da Série A do campeonato brasileiro em ordem alfabética são:'
       f' {sorted(times)}')

print ('\033[36m' '---'*8, 'DRAGAS', '---' *8)
chape = ''
print ('\033[36m' f'A Atlético Goianiense está na {times.index("Atlético Goianiense") + 1}º posição')