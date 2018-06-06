a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento:'))
c = float(input('Digite o terceiro segmento:'))

if a < b + c and b < a + c and c < a + b:
    print('As retas acima formam Triângulo!')
if a == b == c:
    print('O triângulo é equilátero.')
elif a == b or b == c:
    print('O triângulo é isósceles.')
elif a != b != c:
    print('O triângulo é escaleno.')
else:
    print('As retas acima não formam triângulo!')




