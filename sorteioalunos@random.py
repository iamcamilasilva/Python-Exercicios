# Leia o nome de 4 alunos e sorteie 1 deles.

import random

a1 = str(input('Primeiro aluno'))
a2 = str(input('Segundo aluno'))
a3 = str(input('Terceiro aluno'))
a4 = str(input('Quarto aluno'))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))

