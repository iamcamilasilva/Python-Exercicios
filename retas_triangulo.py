# Digite 3 valores para reta e diga se elas formam um triângulo ou não.

r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))

if (r1**2) < (r2**2) + (r3**2) and (r2**2) < (r1**2) + (r3**2) and (r3**2) < (r1**2) + (r2**2):
            print('As retas formam um triangulo')

else:
    print('As retas não formam um triangulo')
