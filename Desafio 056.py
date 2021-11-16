media = 0
somaidade = 0
quantasmulheres = 0
maisvelho = 0
nomevelho = ' '
for a in range (1,500):
    print (f'--------{a}° PESSOA-------')
    nome = str(input('Qual seu nome?')).strip()
    idade = int(input('Qual sua idade?'))
    sexo = str(input('Qual seu sexo? (M/F):')).strip()
    somaidade = somaidade + idade
    media = somaidade / 4
    if a == 1 and sexo == 'Mm':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        quantasmulheres += 1
print(f'A média de idade do grupo é de:{media} anos.')
print (f'{nomevelho} é o homem mais velho do rolê.')
print (f' tem {quantasmulheres} mulheres abaixo de 20 anos no rolê')
