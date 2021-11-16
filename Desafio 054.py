from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for a in range (1,8):
    ano = int (input(f'Em qual ano a pessoa {a} nasceu?'))
    idade = atual - ano
    print (f'Essa pessoa tem {idade} anos.',end=' ')
    if idade >= 18:
        totmaior += 1
        print (f'E já até alcançou a maioridade.',)
    else:
        totmenor += 1
        print (f'E ainda não alcançou a maioridade.')

print (f'Nessa pesquisa, {totmaior} pessoas já alcançaram a maioridade.')
print (f'Nessa pesquisa, {totmenor} pessoas ainda não alcançaram a maioridade.')
