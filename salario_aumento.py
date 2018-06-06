# Leia um valor de salário e diga o seu aumento de acordo com o percentual para cada faixa salarial.

sal = float(input('Digite o valor do seu salario: R$'))

if sal > 1250.00:
    novo = sal + (sal * 0.10)
    print('Seu novo salário com aumento será: R$ {}.'.format(novo))
else:
    novo = sal + (sal * 0.15)
    print('Seu novo salário com aumentg será: R$ {}.'.format(novo))
