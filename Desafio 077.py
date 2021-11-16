#https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=78
#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Desafio', 'Webcam', 'Vem', 'Neosoro', 'Teclado', 'Mouse', 'Unha', 'Cabelo', 'Joelho', 'Caneta')
for p in palavras:
    print (f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')
