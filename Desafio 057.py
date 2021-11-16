#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
#https://www.youtube.com/watch?v=JGztEBLGj5E
a = str(input('Qual seu sexo?(M/F)')).upper().strip()[0]
while a not in 'MF':
    a = str(input('Dados inválidos, por favor, digite novamente:')).upper().strip()[0]
print ('Fim')