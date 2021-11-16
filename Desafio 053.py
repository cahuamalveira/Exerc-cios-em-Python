frase = str(input('Digite uma frase:')) .strip().upper()
palavras = frase.split()
junto = '*'.join(palavras)
inv = ''
for a in range (len(junto)-1,-1,-1):
    inv += junto [a]
    if inv == junto:
        print ('A sua frase é um palíndromo')
    else:
        print ('A sua frase não é um palíndromo')
#https://youtu.be/5VBWe6BXzRo?t=572
