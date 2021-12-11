'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
from time import sleep
while True:
    numero = int(input('Qual número você que a tabuáda: '))
    if numero < 0:
        break
    print('-' * 20)
    print('Tabuada do {}'.format(numero))
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 20)
    sleep(2)
print('Programa finalizado')