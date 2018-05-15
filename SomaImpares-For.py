#Soma dos numeros impares entre 1 e 500, divisiveis por 3.

soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
print('A soma de todos os valores ímpares entre 1 e 500 é: {}'.format(soma))





