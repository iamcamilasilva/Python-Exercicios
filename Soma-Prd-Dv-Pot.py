'Crie um programa que leia 2 numeros e diga seus respectivos: soma, produto, divisão, divisão inteira, potencia'

n1 = int(input('digite um valor:'))
n2 = int(input('digite outro valor:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = pow(2,4)

print('A soma é {}, \n O produto é {}, \n A divisão é {:.3f} ' .format(s,m,d), end ='')
print('A divisão inteira é {},\n A potencia é {}' .format(di,e))


