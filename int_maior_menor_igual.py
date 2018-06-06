# Digite dois valores e compare se eles são maiores, menores ou iguais entre si.

n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))

if n1 > n2:
    print('O primeiro número {} é maior que o segundo número {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é maior que o primeiro {}.'.format(n2, n1))
elif n1 == n2:
    print('O primeiro número {} é igual ao segundo número {}'.format(n1, n2))
else:
    print('Opção inválida!')
