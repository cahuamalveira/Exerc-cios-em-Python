#https://www.youtube.com/watch?v=X0a5aZg93Uc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=68
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Qual número você quer ver a tabuada?'.strip()))
    if n < 0:
        break
    for a in range (1, 11):
        tabu = n * a
        print(f'{n} x {a}: {n * a}')
print ('Acaboou')
