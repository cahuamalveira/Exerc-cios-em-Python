#https://www.youtube.com/watch?v=uk0gDFQEo_I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=83
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
listanormal = list()
listapar = list()
listaimpar = list()
while True:
    listanormal.append(int(input('Digite um número:')))
    usuario = str(input('Você deseja continuar?[S/N]').strip())
    if usuario in 'NnNãoNaonãoNÃOnaoNAO':
        break
for c, v in enumerate(listanormal): #não entendo o que é esse c
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(c)
print (f'Essa é a lista de todos os números digitados: {listanormal}')
print (f'Essa é a lista de todos os números PARES digitados: {listapar}')
print (f'Essa é a lista de todos os números ÍMPARES digitados: {listaimpar}')