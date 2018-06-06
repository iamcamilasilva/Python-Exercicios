#Faça um programa que leia o nome, idade e sexo de 4 pessoas e na saída mostre:
#A media de idade do grupo, o nome do homem mais velho, quantas mulheres tem menos de 20.

for c in range(0, 4):
    nome = str(input('Digite o seu nome:'))
    idade = int(input('Digite a sua idade:'))
    #sexo = str(input('Digite seu sexo:'))

    media = (c + idade) / 4

print('A media de idade do grupo é {}.'.format(media))

    #print('A media de idade do grupo é {}. \n O nome do homem mais velho é {}. \n Há {} mulheres com menos de 20.'.format(media))
