'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

'''num = input('Digite um número:')
list = list(num)
uni = list[0]
dez = list[1]
cent = list[2]
mil = list[3]
print('Analizando o número: {}'. format(num))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(mil))'''


# Resolver o problema como String:

'''num = int(input('Digite um número: '))
n = str(num)
print('Analisando o nùmero:')
print('Unidade:{}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar {}'.format(n[0]))'''

#Resolver matematicamente:

num = int(input('Digite um número: '))
u = num // 1 % 10
# Pega o número, divide por 1 e tira o modulo de 10 (divide o número por 10 e pega o resto da divisãoão)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o nùmero:')
print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Centena:{}'.format(c))
print('Milhar {}'.format(m))

