import random
num = str(random.randint(0, 9999))
print (num)
print (f'Milhar: {num[0:1]}')
print (f'Centena: {num [1:2]}')
print (f'Dezena: {num[2:3]}')
print (f'Unidade:{num [3:4]}')