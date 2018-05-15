#Faça um programa que leia e atualize o saldo do cartão de passagem do usuário. Para recargas feitas antes da data do aumento cobrar o valor de R$ 3,80. Para as demais, cobrar o valor de R$ 4,00.

from datetime import date

saldo = float(input('Passe o seu cartão de passagem:'))

recarga = date.today().year
date = date.today()

if recarga < date:
    sfinal = saldo - 3.80
    print('O seu novo saldo é: {:.2f}'.format(sfinal))
else:
    sfinal = saldo - 4.00
    print('O seu novo saldo é {:.2f}'.format(sfinal))

