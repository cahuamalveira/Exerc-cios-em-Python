from random import randint
vel = randint(0, 300)
print (f'Você estava andando a {vel}km/h.')
if vel >80:
    print (f'Pelo limite da via ser 80km/h e você estar conduzindo o veículo a {vel}km/h, você será multado em R${(vel-80)*7},00')
else:
    print (f'Você estava dentro do limite de velocidade dirigindo a {vel}km/h, pode seguir viagem.')