# Digite um numero real com casas decimais e leia apenas a parte inteira.

import math

n = float(input('Digite um numero:'))

int = math.trunc(n)

print('O numero inteiro é {}:'.format(int))

