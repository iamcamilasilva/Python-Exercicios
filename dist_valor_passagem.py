# Digite a distancia em km da sua viagem e veja o valor da passagem.

dist = float(input('Qual a distancia da sua viagem em Km?'))

if dist <= 200:
    prc = dist * 0.50
    print('O valor da sua passagem será: {} reais.'.format(prc))
else:
    prc = dist * 0.45
    print('O valor da sua passagem será: {} reais.'.format(prc))
