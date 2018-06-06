# Calcula a raizquadrada de um número com a opção de: arredondar para menos, valor exato(com 2 pontos flutuantes) e arredondando para mais. Usando a biblioteca math.
from math import sqrt, floor, ceil

num = int(input('Digite um numero:'))

raiz = sqrt(num)

print('A raiz quadrada de {} é: {}'.format(num, ceil(raiz)))
print('A raiz quadrada de {} é: {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} é: {}'.format(num, floor(raiz)))

