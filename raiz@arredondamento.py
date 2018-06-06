# Calcula a raizquadrada de um número com a opção de: arredondar para menos, valor exato(com 2 pontos flutuantes) e arredondando para mais.
import math


num = int(input('Digite um numero:'))

raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))         #arredonda pra cima
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))                    #raiz real
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))        #arredonda para baixo


