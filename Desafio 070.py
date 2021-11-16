#https://www.youtube.com/watch?v=hS8QdW-1HTo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=40
#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 
soma = cont = menor = maisqmil= 0
nome = ''
while True:
     produto = str(input('Qual o produto?').strip())
     valor = float(input ('Qual o valor desse produto?'.strip()))
     cont += 1
     soma = valor + soma
     if valor > 100:
          maisqmil +=1
     if cont == 1 or valor < menor:
          menor = valor
          nome = produto
     resp = ''
     pergunta = str(input('Você deseja continuar? [S/N]'.strip()))
     if pergunta not in 'Ss':
          print ('Muito obrigado pela participação.')
          break
print (f'O total da compra foi de:R${soma}')
print (f'Tiveram {maisqmil} produtos que valem mais de 1000.')
print (f'O produto mais barato foi: {nome}.')


