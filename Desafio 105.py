"""https://youtu.be/Kbs97l38vVQ
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:
- Quantidade de notas
- A maior nota CHECK
- A menor nota Check
- A média da turma CHECK
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""

from time import sleep

def boletim():
    notas = dict()
    notas['Notas'] = []
    cont = 0
    while True:
        #n1 = list
        n1 = float(input('Qual sua nota?'))
        notas['Notas'].append(n1)
        usuario = input('Deseja continuar?')
        cont += 1
        if usuario in 'NnNÃOnaonn':
            break
    print(notas['Notas'])
    print(f'A maior nota foi: {max(notas["Notas"])}')
    print(f'A menor nota foi: {min(notas["Notas"])}')
    print(f'A média das notas é de: {sum(notas["Notas"]) / cont}')
    sleep(0.5)
    if sum(notas["Notas"]) / cont >= 6:
        print('Você está aprovado!')
    else:
        print('Você está reprovado!')


boletim()




"""def notas():
    cahua = list()
    media = 0
    situação = ''
    cahua = float(input('Qual sua nota?'))
    return cahua.__dict__
print(cahua)"""


