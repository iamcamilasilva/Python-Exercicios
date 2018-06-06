# Leia o ano e diga se ele é bissexto.

import datetime
ano = int(input('Qual a ano voce deseja consultar?'))

a = ano % 4
b = ano % 100
c = ano % 400

if ano == 0:
    ano = datetime.date.today().year
if a == 0 and b != 0 or c == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')

