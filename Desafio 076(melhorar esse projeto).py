#https://www.youtube.com/watch?v=Qp2cXfCHk2I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=77
#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print ('---'*30)
print('                                       LISTA DE PREÇOS')
print ('---'*30)
preços = ('Brahma', 3.50,
          'Heineken', 5.00,
          'Bauducco de morango', 1.50,
          'Pringles', 11.00,
          'Velho Barreiro', 15.50,
          'Gibi da Turma da Mônica', 7.00,
          'Camisa do Atlético Goianiense', 179.99,)
for pos in range (0, len(preços)):
    if pos % 2 == 0:
        print (f'{preços[pos]:.<60}', end='')
    else:
        print (f'R${preços[pos]:.2f}')