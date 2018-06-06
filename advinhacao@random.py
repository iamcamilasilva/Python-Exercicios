# Digite um inteiro entre 0 e 5. O computador irá sortear um numero nesse range e informará se vc acertou ou errou.

import random
import time

nd = int(input('Digite um numero inteiro entre 0 e 5:'))
n = random.randint(0, 5)
print('Processando...')
time.sleep(3)
if nd == n:
    print('Voce acertou! Parabéns!')
else:
    print('Que pena! Voce errou! O numero escolhido foi {}'.format(n))
