homens = mulheres = idade = contag = menor = 0
usuario = ''
while True:
     sexo = str(input('Qual seu sexo?[M/F]'.strip()))
     if sexo == 'M':
         homens += 1
     else:
         mulheres += 1
     idade = int(input('Qual sua idade?'.strip()))
     if sexo == 'F' and idade < 20:
         menor += 1
     if idade > 18:
         contag += 1
     usuario = str(input('Você deseja continuar?[S/N]'.strip()))
     while usuario not in 'SN':
        usuario = str(input('Você deseja continuar?[S/N]'.strip()))
     if usuario == 'N':
        print ('E acabooou brasileirinho')
        break
print (f'Foram registrados {homens} homens.')
print (f'Foram registrados {mulheres} mulheres.')
print (f'Foram registrados {contag} pessoas que tem mais de 18 anos.')
print (f'Foram registrados {mulheres} mulheres, e {menor} delas são abaixo de 20 anos.')





