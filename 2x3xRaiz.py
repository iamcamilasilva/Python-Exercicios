# Digite um numero e informe o dobro, triplo e raiz quadrada.

n1 = int(input('Digite um numero:'))

d = 2 * n1
t = 3 * n1
r = n1 ** (1/2)

print('O dobro é: {}, O triplo é: {}, A raiz quadrada é: {:.2f}'.format(d, t, r))
