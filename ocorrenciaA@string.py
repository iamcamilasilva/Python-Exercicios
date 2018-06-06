# Informe a ocorrencia de vezes e posição de uma letra em uma string.

frase = str(input('Digite uma frase:')).strip().lower()

print('A letra A aparece {} vezes.'.format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('a')+1))
print('A letra A aparece pela ultima vez na posição {}.'.format(frase.rfind('a')+1))

