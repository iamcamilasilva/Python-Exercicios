# Digite um numero inteiro e converta para as bases: binario, octal e hexadecimal.

import para as para

num = int(input('Digite um numero inteiro:'))

print('Escolha uma das bases abaixo para conversão: \n [ 1 ] converte para BINÁRIO \n [ 2 ] converte para OCTAL \n [ 3 ] converte para hexadecimal')

opcao = int(input('Sua opção:'))

if opcao == 1:
    print('{} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}:'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA! TENTE OUTRA VEZ!')






