'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

color = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yelow': '\033[1;33m', 'green': '\033[1;32m',
         'purple': '\033[1;35m', 'clean': '\033[m'}

seg_1 = int(input('Primeiro seguimento: '))
seg_2 = int(input('Seguando seguimento: '))
seg_3 = int(input('Terceiro seguimento: '))

if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    print('As retas acima PODEM FORMAR um triângulo!', end='')
    if seg_1 == seg_2 and seg_2 == seg_3:
        print('{}EQUILÁTERO!{}'.format(color['blue'], color['clean']))
    elif seg_1 != seg_2 != seg_3 != seg_1:
        print('{}ESCALENO!{}'.format(color['green'], color['clean']))
    else:
        print('{}ISÓSCELES!{}'.format(color['yelow'], color['clean']))
else:
    print('As retas acima {}NÃO PODEM{} Formar triângulo!'.format(color['red'], color['clean']))
