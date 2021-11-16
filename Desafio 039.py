dat = int(input('Em qual ano você nasceu?'))
idad = 2020 - dat
if idad <18:
    print (f'Você ainda não precisa participar do alistamento militar obrigatório.')
elif idad>18:
    print ('Você já passou da idade de fazer alistamento militar. Realmente espero que você já tenha feito kkk.')
elif idad ==18:
    print ('Você está na idade para fazer o alistamento militar obrigatório.')
