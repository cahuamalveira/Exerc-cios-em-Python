#https://youtu.be/7xrCJnniqMw
#Crie um programa que leia nome e nota de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
#Aluno individualmente.
aluno = list()
while True:
    nome = str(input('Nome:'.strip()))
    nota1 = float(input('Nota 1:'.strip()))
    nota2 = float(input('Nota 2:'.strip()))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    usuario = str(input('Você deseja continuar?'.strip()))
    if usuario in 'NnNÃOnãonnNãonaoNAO':
        break
print(f'{"No.":<4} {"Nome":<10} {"Média":>8}')
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno?(999 interrompe)'.strip()))
    if opc == 999:
        print('obrigado e Adeus')
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
print(f'Obrigadooooo')