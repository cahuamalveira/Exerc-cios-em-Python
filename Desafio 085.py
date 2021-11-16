#https://youtu.be/2-fy24bbMJ4
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
impar = []
par = []
todos = []
num = []
top = 0
for num in range(0, 7):
    top = int(input('Digite um número:'.strip()))
    if top % 2 == 0:
        par.append(top)
    if top % 2 != 0:
        impar.append(top)
    todos.append(top)
print(f'Os números pares digitados são: {par}')
print(f'Os números ímpares digitados são: {impar}')
print(f'{sorted(todos)}')


