import math
val = float(input('Qual o valor da casa?'))
sal = float(input('Qual o seu salário?'))
praz = int(input('Em quantos anos você irá pagar a casa?'))
prest = val / praz * 12
nn = (30/100 * sal)
print ('O valor da prestação mensal será de R$ {:.2f}'. format (prest))
if prest > nn:
    print ('Parabéns o empréstimo irá ocorrer tranquilamente sem maiores problemas')
if prest < nn:
    print ('O empréstimo foi negado.')
