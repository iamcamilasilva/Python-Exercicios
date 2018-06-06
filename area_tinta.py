# Calcule as dimensões da sua parede e calcule quantos litros de tinta será necessário para pintá-la.

n1 = float(input('Qual a altura da sua parede?'))
n2 = float(input('Qual a largura da sua parede?'))

area = n1 * n2
lt = area / 2

print('A sua parede possui area de: {:.2f}m² \n Precisara de {:.2f}l para pinta-la'.format(area, lt))
