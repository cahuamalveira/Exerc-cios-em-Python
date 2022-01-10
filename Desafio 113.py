"""https://youtu.be/KowQ_UIMuI8
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""
from ÚTEIS import cores


def leiaInt(texto):
    valor = 0
    ok = False
    while True:
        n = str(input(f'{texto}'))
        if n.isnumeric():
            valor = int(n)
            ok = True
        if ok:
            break
        return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')