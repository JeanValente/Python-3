'''Exercício Python 18: Faça um programa que leia um ângulo qualquer
 mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

'''import math
ângulo = float(input('Digite o angulo que voê deseja:'))
seno = math.sin(math.radians(ângulo))
coseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} graus, tem o SENO de {:.2f}, o COSENO de {:.2f} e a TANGENTE de {:.2f}'.format(int(ângulo), seno, coseno, tangente))'''

# De um modo mais simplificado, pode importar só o que vai usar

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que voê deseja:'))
seno = sin(radians(ângulo))
coseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} graus, tem o SENO de {:.2f}, o COSENO de {:.2f} e a TANGENTE de {:.2f}'.format(int(ângulo), seno, coseno, tangente))