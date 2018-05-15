#Faça um programa que leia a 6 numeros inteiros e de a soma apenas dos numeros pares digitado.

s = 0
for c in range(0, 6):
    valor = int(input('Digite 6 numeros inteiros:'))
    if valor % 2 == 0:
        s += valor
print('A soma dos valores pares digitados é: {}'.format(s))


