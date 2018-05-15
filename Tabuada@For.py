# Faça um programa que calcule a tabuada de qualquer numero que o usuario escolher utilizando @For.

numero = int(input('Digite o numero da tabuada que você deseja consultar:'))
print('Tabuada de {} é:'.format(numero))

for c in range(0, 10+1):
    print('{} * {} = {}'.format(numero, c, numero * c))
