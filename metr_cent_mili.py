# Digite um valor e converta para centimetros e milimetros.

n1 = float(input('Entre com o valor em metros:'))

cent = n1 * 100
mil = n1 * 1000

print('O valor em centimetros é: {:.3f} \n O valor em milimetros é: {:.3f}'.format(cent, mil))

