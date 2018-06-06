# Leia o valor de uma compra, opção de pagamento e informe o desconto para cada modalidade: dinheiro, cheque, cartão ou parcelado.

valor = float(input('Qual o valor da sua compra? R$'))
print('Qual será a forma de pagamento: \n [ 1 ]DINHEIRO | CHEQUE \n [ 2 ]CARTÃO DE CRÉDITO A VISTA \n [ 3 ]2x NO CARTÃO DE CRÉDITO \n [ 4 ]3x OU MAIS NO CARTÃO DE CRÉDITO')
opcao = int(input('Qual a opção de pagamento?'))

if opcao == 1:
    vafinal = valor - (valor * 0.10)
    print('O valor a pagar pela sua compra de R${:.2f}, será R${:.2f}.'.format(valor, vafinal))
elif opcao == 2:
    vafinal = valor - (valor * 0.05)
    print('O valor a pagar pela sua compra de R${:.2f}, será R${:.2f}.'.format(valor, vafinal))
elif opcao == 3:
    vafinal = valor / 2
    print('O valor a pagar pela sua compra de R${:.2f}, será de 2 parcelas fixas no valor de R${:.2f}.'.format(valor, vafinal))
elif opcao == 4:
    n = int(input('Em quantas vezes você deseja parcelar?'))
    vafinal = (valor + (valor * 0.20)) / n
    print('O valor a ser pago pela sua compra de R${:.2f}, será de {} parcelas fixas no valor de  R${:.2f}.'.format(valor, n, vafinal))
else:
    print('\033[31m OPÇÃO INVÁLIDA. TENTE NOVAMENTE. \033[m')



