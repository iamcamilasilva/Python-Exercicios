#Faça um programa que leia um numero inteiro e diga se ele é um numero primo.

n = int(input('Digite um valor inteiro:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Logo ele é primo!')
else:
    print('Logo ele não é primo')


