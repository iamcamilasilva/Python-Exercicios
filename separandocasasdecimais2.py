# """Faça um programa que elia um número de 0 a 9999 e mostre na tela cada um dos digitos separados"""

numero = str(input('Digite qualquer numero:')).strip()

print('Analisando o numero {}'.format(numero))
print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))




