# """Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados"""

num = int(input('Digite qualquer numero:')).strip()

u = num // 0.1
d = num // 1
c = num // 10
m = num // 100

print('Analisando o numero {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))