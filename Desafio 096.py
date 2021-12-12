#https://youtu.be/oV1s53YGtvE
#Faça um programa que tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de {largura} x {comprimento} é: {a} metros quadrados.')

l = float(input('Qual a largura do terreno?'.strip()))
c = float(input('Qual o comprimento do terreno?'.strip()))
area(l, c)
#print(area)
