#https://www.youtube.com/watch?v=q8Z1cRdJnfk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=79
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for cont in range (0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont + 1}:')))
print ('---' *30)
print (f'O maior valor digitado foi: {max(lista)} na posição: {lista.index(max(lista)) + 1}')
print (f'O menor valor digitado foi: {min(lista)} na posição {lista.index(min(lista)) + 1}')
for c, v in enumerate(lista):
    print (f'Na posição {c + 1} foi digitado o valor: {v}')
print ()

