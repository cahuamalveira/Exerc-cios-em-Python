import math
n1 = float(input ('Qual o valor do cateto oposto?'))
n2 = float (input ('Qual o valor do cateto adjascente?'))
hip = math.hypot(n1, n2)
print ('A hipotenusa vale: {:.3}' .format (hip))
