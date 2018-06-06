# Leia um nome e diga true se tiver silva e false se não tiver silva.

nome = str(input('Qual é o seu nome?')).strip()

print('O seu nome tem silva? {}'.format('silva' in nome.lower()))



