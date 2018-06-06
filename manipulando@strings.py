# Manipulando Strings.

nome = str(input('Me diga o seu nome:')).strip()

print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
print('seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem letras {}'.format(separa[0], len(separa[0])))
















