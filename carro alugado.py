# 'Crie um programa que leia de um carro alugado quantos dias e quantos km foram utilizados e calcule o valor total a ser pago'


d = int(input('Quantos dias de aluguel?'))
k = float(input('Quantos km rodados?'))

p = (d * 60.0) + (k * 0.15)

print('O valor total a ser pago é: R${:.2f}'.format(p))
