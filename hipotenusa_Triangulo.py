# Leia o valor dos catetos de um triangulo e informe o valor da hipotenusa.

import math

a = float(input('Digite o valor do cateto adjacente:'))
b = float(input('Digite o valor do cateto oposto:'))

c = math.hypot(a,b)

print('O valor da hipotenusa entre {} e {}, é {:.2f}:'.format(a, b, c))

