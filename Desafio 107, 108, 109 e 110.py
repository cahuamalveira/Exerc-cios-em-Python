# EXERCÍCIO 107
""""https://youtu.be/y8pI8YBphQI
Crie um módulo chamado moeda.py que tenha as funções incorporadas
 aumentar(), diminuir(), dobro(CHECK) e metade(CHECK).
Faça também um programa que importe esse módulo e use algumas dessas funções."""
# ======================================================================================================================
# EXERCÍCIO 108
"""https://youtu.be/KtRkGEeUdqE
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
valor monetário formatado."""
#=======================================================================================================================
#EXERCÍCIO 109
"""https://youtu.be/Y0zNYTHoGhQ
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""
#=======================================================================================================================
#EXERCÍCIO 110
"""https://youtu.be/1Ks218WINT8
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

#from time import sleep

#CÓDIGO DOS DESAFIOS 107 E 108
"""p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))} ')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 20%, temos: {moeda.moeda(moeda.diminuir(p, 20))}')"""
#CÓDIGO DESAFIO 109
"""h = float(input('Digite o preço: R$'))
sleep(0.5)
print(f'A metade de {moeda.moeda(h)} é: {moeda.metade(h, True)} ')
sleep(0.5)
print(f'O dobro de {moeda.moeda(h)} é: {moeda.dobro(h, True)}')
sleep(0.5)
print(f'Aumentando 10%, temos: {moeda.aumentar(h, 10, True)}')
sleep(0.5)
print(f'Diminuindo 20%, temos: {moeda.diminuir(h, 20, True  )}')"""
#CÓDIGO DESAFIO 110
from Exercícios.desafioPython.UtilidadesCemV import moeda
from Exercícios.desafioPython.UtilidadesCemV import dados


h = dados.leiadinheiro('Digite o preço: R$'.strip())
moeda.resumo(h, 73, 14)