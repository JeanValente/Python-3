'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1
print('O número {} foi divisível por {} números'.format(numero, tot))
if tot == 2:
    print('Ele é um número primo')
else:
    print('Ele não é um número primo')
