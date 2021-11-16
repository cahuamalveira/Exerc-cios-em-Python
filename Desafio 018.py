import math
ang = int(input ('Qual o ângulo que cê quer saber?'))
cos = math.cos (math.radians(ang))
tang = math.tan(math.radians (ang))
seno = math.sin(math.radians (ang))
print (f'O cosseno do de {ang:.4f}º é {cos:.2f}º\n A tangente de {ang:.2f}º é {tang:.2f}º\n E o seno de {ang:.2f}º é {seno:.2f}º')
