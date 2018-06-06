'Crie um programa que leia o salário atual de um funcionário e diga o seu valor com 15% de aumento'

s = float(input('Entre com o seu salario atual: R$'))

ns = s + (s * 0.15)

print('O seu novo salario com aumento é: {:.2f}'.format(ns))

