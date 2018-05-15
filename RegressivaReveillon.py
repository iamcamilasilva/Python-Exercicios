#Faça um programa que crie uma contagem regressiva para os fogos artificios de Ano Novo.
#A contagem deve ser regressiva, começar em 10 e terminar em 0. Com pausa de 1s entre eles.

from time import sleep
for c in range(10, 0, -1):
    print(c);
    sleep(1);
print('Feliz Ano Novo!')
