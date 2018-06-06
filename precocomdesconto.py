# Clacular preço de um produto com desconto.

n1 = float(input('Leia o preço do produto:'))

pd = n1 - (n1 * 0.05)

print('O preço do produto com desconto é: {:.2f}'.format(pd))
