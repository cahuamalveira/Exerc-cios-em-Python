a = float(input('Qual a medida do cateto oposto do triângulo em centímetros?'))
b = float (input('Qual a medida do cateto adjascente do triângulo em centímetros?'))
c = float (input('Qual a medida da hipotenusa do triângulo em centímetros?'))
if a < b + c and a < c + b and b < c + a:
    print ('É possível formar um triângulo com os valores acima.')
else:
    print ('Não é possível formar um triângulo com os valores propostos')