# Jogo pedra, papel, tesoura.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('Escolha uma opção: \n [ 0 ]PEDRA \n [ 1 ]PAPEL \n [ 2 ]TESOURA')
escolha = int(input('Qual é a sua escolha?'))

print('Computador jogou {}.Você jogou {}'.format(itens[computador], itens[escolha]))

if computador == 0:
    if escolha == 0:
         print('DEU IMPATE!')
    elif escolha == 1:
         print('JOGADOR VENCEU!')
    elif escolha == 2:
         print('COMPUTADOR VENCEU!')
    else:
         print('\033[31m OPÇÃO INVÁLIDA! TENTE NOVAMENTE! \033[m')
elif computador == 1:
    if escolha == 0:
         print('COMPUTADOR VENCE!')
    if escolha == 1:
         print('DEU IMPATE!')
    elif escolha == 2:
         print('JOGADOR VENCE!')
    else:
         print('\033[31m OPÇÃP INVÁLIDA! TENTE NOVAMENTE! \033[m')

elif computador == 2:
    if escolha == 0:
        print('JOGADOR VENCE!')
    if escolha == 1:
        print('COMPUTADOR VENCE!')
    elif escolha == 2:
        print('DEU IMPATE!')
    else:
        print('\033[31m OPÇÃO INVÁLIDA! TENTE NOVAMENTE! \033[m')
