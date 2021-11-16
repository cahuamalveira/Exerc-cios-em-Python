name = str(input('Digite seu nome:'))
print (name.find('Silva'))
print ('Se o número apresentado for maior que 0, o nome digitado possui Silva em sua formação.')

#divisor de águas

nome = str(input('Digite seu nome:')).strip()
print ('Seu nome tem Silva? {}' .format ('silva' in nome.lower()))