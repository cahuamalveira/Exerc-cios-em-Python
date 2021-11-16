import random
aa = (input('Primeiro aluno:'))
ab = (input ('Segundo aluno:'))
ac = (input('Terceiro aluno:'))
ad = (input ('Quarto aluno:'))
ae = (input ('Quinto aluno:'))
list = [aa, ab, ac, ad, ae]
random.shuffle (list)
print ('A sequência de grupos que irão se apresentar será, respectivamente:')
print (list)