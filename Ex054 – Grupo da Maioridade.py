'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
soma = 0
cont = 0
for c in range(1, 8):
    data = int(input('Digite a data:'))
    idade = date.today().year - data
    if idade >= 18:
        cont += 1
print('Do total de {} pessoas, {} são maiores de idade e {} são menores'.format(c, cont, c - cont))