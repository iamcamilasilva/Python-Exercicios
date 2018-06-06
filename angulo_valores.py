# Leia o valor de um angulo e informe os valores: seno, cosseno e tangente.

import math

a = float(input('Digite o valor do angulo:'))

s = math.sin(math.radians(a))
c = math.cosh(math.radians(a))
t = math.tan(math.radians(a))

print('O valor de seno é {:.2f} \n O valor de cosseno é {:.2f} \n O valor de tangente é {:.2f}'.format(s, c, t))
