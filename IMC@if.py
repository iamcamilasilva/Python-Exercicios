# Leia o peso e a altura, faça o calculo do IMC e diga em que faixa se classifica: abaixo, no peso, sobrepeso ou obesidade.

peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))

imc = peso / pow(altura,2)

print('O seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Voce está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você está com obesidade morbida!')