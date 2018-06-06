# Alistamento Militar. Leia o sexo. Se feminino, não precisa se alistar. Se masculino, informe em que ano será ou se passou do prazo.

from datetime import date
from time import sleep

sexo = str(input('Selecione o seu sexo abaixo: \n [1]Feminino \n [2]Masculino'))
opcao = int(input('Sua opcao:'))

if opcao == 1:
    print('VOCE E DO SEXO FEMININO. NAO PRECISA SE ALISTAR!')
    sleep(2)

nascimento = int(input('Se você for do sexo masculino, em que ano vc nasceu?'))
aatual = date.today().year
idade = aatual - nascimento

if idade == 18:
       print('Você deverá se alistar esse ano!')
elif idade < 18:
    saldo = 18 - idade
    ano = aatual + saldo
    print('Você possui {} anos. Ainda não está na época de você se alistar.Faltam {} anos para você se alistar, isso ocorrerá em {}!'.format(idade,saldo, ano))
elif idade > 18:
    saldo = idade - 18
    ano = aatual - saldo
    print(' Você deveria ter se alistado há {} anos. No ano de {}. REGULARIZE A SUA SITUAÇÃO!'.format(saldo, ano))








