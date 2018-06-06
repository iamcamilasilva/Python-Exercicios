# Leia um nome completo e informe o 1º e ultimo nome.

nome = str(input('Digite o seu nome completo:')).strip()

nome = nome.split()

print('Muito prazer em te conhecer!!!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))


