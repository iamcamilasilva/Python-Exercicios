# Emprestimo Imobiliario. leia os valores do imóvel, sal e anos de prestação e veja se atende as condições para emprestimo.

casa = float(input('\033[32;m Qual o valor da casa que voce deseja comprar? R$\033[m'))
sal = float(input('\033[32;m Qual o valor do seu salário? R$\033[m'))
anos = float(input('\033[32;m Em quantos anos voce deseja pagar as prestações? \033[m'))


pres = casa / (anos * 12)
min = sal * 0.30

if pres <= min:
    print('EMPRESTIMO APROVADO!')
    print('Você pode comprar a casa no valor de R${:.2f}, com prestação mensal de R${:.2f}'.format(casa, pres))
else:
    print('EMPRESTIMO NEGADO!')
    print('Você não pode comprar a casa no valor de R${:.2f} pois o valor está acima de 30% do seu salário'.format(casa))

