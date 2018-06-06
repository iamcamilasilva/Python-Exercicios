# Digite a velocidade do seu carro e veja se voce está ou não dentro do limite de velocidade e o valor da multa, caso voce tenha sido multado.

km = float(input('Qual a velocidade do seu carro?'))

if km <= 80.00:
    print('Voce está dentro do limite de velocidade permitido. Parabéns!')
else:
    v = (km -80) * 7
    print('Voce ultrapassou o limite de velocidade permitido. Voce foi multado em, {} reais.'.format(v))
