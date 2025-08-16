import math

co = float(input('Digite o comprimento do cateto oposto do tringulo: '))
ca = float(input('Digite o comprimento do cateto adjacente do tringulo: '))
h = math.sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa é: {:.2f} '.format(h))