'''Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = input('Digite seu nome:').strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

# "in" é um operador para encontrar (tentei .find e não deu certo)

