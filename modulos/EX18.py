from math import sin, cos, tan

ang = float(input('Digite o valor de um ângulo: '))
angr = ang * 3.14 / 180   #poderia ter usado a função "radians"
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f} '.format(sin(angr), cos(angr), tan(angr)))
