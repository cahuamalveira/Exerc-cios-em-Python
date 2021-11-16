import random
pa = (input ('Digite o nome do primeiro aluno:'))
pb = (input ('Digite o nome do segundo aluno:'))
pc = (input ('Digite o nome do terceiro aluno:'))
pd = (input ('digite o nome do quarto aluno:'))
list = [pa, pb , pc, pd]
escolha = random.choice (list)
print (f'O aluno sorteado pelo professor para apagar o quadro foi: {escolha}')