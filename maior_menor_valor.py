# Leia 3 valores e diga quais são maiores e menores entre eles.

n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
n3 = float(input('Digite o terceiro numero:'))

menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
