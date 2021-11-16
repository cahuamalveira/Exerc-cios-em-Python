dist = int(input('Qual a distância em KM para essa cidade?'))
if dist <200:
    print (f'A passagem irá custar: R${dist * 0.50}')
else:
    if dist >200:
        print (f'A passagem irá custar: R${dist*0.45}')