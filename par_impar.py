# Digite um numero e saiba se ele é par ou impar.

n = int(input('Digite um numero:'))

r = n % 2

if r != 0:
    print('O numero é impar!')
else:
    print('O numero é par!')
