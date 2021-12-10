'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''
cores = {'clean':'\033[m', 'red':'\033[1;31m', 'yelow':'\33[1;33m', 'blue':'\033[1;34m', 'green':'\033[1;32'}
print('=-='*20)
print('            Analisador de triangulos')
print('=-='*20)
seg_1 = int(input('Primeiro seguimento: '))
seg_2 = int(input('Seguando seguimento: '))
seg_3 = int(input('Terceiro seguimento: '))

if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    print('As retas acima PODEM FORMAR triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR triângulo!')
