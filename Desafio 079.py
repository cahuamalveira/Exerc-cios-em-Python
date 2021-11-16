#https://www.youtube.com/watch?v=LkAzRnc_GPk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=80
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    n = (int(input('Digite um valor:')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print ('Valor duplicado, tente novamente!')
    #if n == n:
        #print ('Isso é repetido, não vou adicionar')
    usuario = str(input('Deseja continuar? [S/N]'.strip()))
    if usuario in 'NnNãonaonãoNÃO':
        print('Obrigado e adeus')
        break
print (f'Você digitou os valores: {sorted(lista)}')
