# Digite duas notas e diga se o aluno está aprovado, recuperação ou reprovado.

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1 + n2) / 2

if media >= 7.00:
    print('A sua media foi {:.2f}. Voce esta APROVADO(A)!!! PARABENS!!!'.format(media))
elif media < 7.00 and media >= 5:
    print('A sua média foi {:.2f}. Voce esta de recuperação!!!'.format(media))
elif media < 5:
    print('A sua media foi {:.2f}. Você está reprovado!'.format(media))

