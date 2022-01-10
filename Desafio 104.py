"""https://youtu.be/VrQmMbPpbf0
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico."""

def leiaInt(texto):
    valor = 0
    ok = False
    while True:
        n = str(input(f'{texto}'))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Dado inválido! Digite novamente!')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')