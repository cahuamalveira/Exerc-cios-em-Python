print ('Bem vindo a nossa simulação de empréstimo, vamos começar!')
casa = float (input('Qual o valor da casa que você deseja comprar?'))
salario = float (input ('Qual o seu salário?'))
temp = float (input ('Em quantos anos você pretende quitar essa casa?'))
prest = casa / temp
porc = (30/100) * salario
if porc > salario:
    print('Sem empréstimo irá ser negado')
else:
    print ('Seu empréstimo será aprovado')