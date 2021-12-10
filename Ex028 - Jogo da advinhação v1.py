'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
print('Vamos jogar um jogo?')
sleep(2)
num1 = (randint(0, 5))
num2 = int(input('Em que número de 0 a 5 eu estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if num1 == num2:
    print('Parabéns!')
    sleep(1)
    print('Você venceu!')
    sleep(2)
    print('Dessa vez...')
else:
    print('Você errou!')
    sleep(1)
    print('O numero que eu pensei era {}'.format(num1))
    sleep(1)
    print('Sua alma é minha!')
    sleep(2)
    print('MUAHAHAHAHA!')

