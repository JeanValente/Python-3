'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

color = {'blue':'\033[1;34m', 'red':'\033[1;31m', 'yelow':'\033[1;33m', 'green':'\033[1;32m', 'purple':'\033[1;35m', 'clean':'\033[m'}
from datetime import date

nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: {}MIRIM{}.'.format(color['red'], color['clean']))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}.'.format(color['yelow'], color['clean']))
elif idade <= 19:
    print('Classificação: {}JÚNIOR{}.'.format(color['green'], color['clean']))
elif idade <= 25:
    print('Classificação: {}SÊNIOR{}.'.format(color['blue'], color['clean']))
else:
    print('Classificação: {}MASTER{}.'.format(color['purple'], color['clean']))