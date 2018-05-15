#Faça um programa que leia o 1º termo e a razao de uma PA e... No final mostre os 10 primeiros termos da PA.

a1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
decimo = a1 + 10 * r

for c in range(a1, decimo, r):
    print('{}'.format(c))
















