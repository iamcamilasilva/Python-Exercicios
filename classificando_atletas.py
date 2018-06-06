# Leia o ano de nascimento e diga em qual modalidade o atleta se encontra.

from _datetime import date

nasc = int(input('Digite o ano do seu nascimento:'))

idade = date.today().year - nasc

if idade <= 9:
    print('Você é um atleta Mirim!')
elif idade >= 10 and idade <= 14:
    print('Você é um atleta infantil!')
elif idade >= 15 and idade <= 19:
    print('Você é um atleta Junior!')
elif idade >= 20 and idade <= 25:
    print('Você é um atleta Senior!')
elif idade >= 26:
    print('Você é um atleta Master!')

