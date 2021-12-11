'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep
print('Vamos jogar Jokenpô!!')
itens = ('Pedra', 'Papel', 'Tesoura')
machine = randint(0, 2)
player = int(input('''Escolha uma opção:
[0] Pedra
[1} Papel
[2] Tesoura
: '''))
if player > 2:
    print('Jogada invalida!')
    exit()
print('JÔ')
sleep(1)
print("KEN")
sleep(1)
print('PO!!!')
print('A máquina jogou {}'.format(itens[machine]))
print('Você escolheu {}'.format(itens[player]))

elif machine == 0:
    if player == 0:
        print('Empate!')
    elif player == 1:
        print('Jogador Venceu!')
    elif player == 2:
        print('A máquina venceu!')
    else:
        print(('Jogada invalida'))
elif machine == 1:
    if player == 1:
        print('Empate!')
    elif player == 2:
        print('Jogador Venceu!')
    elif player == 0:
        print('A máquina venceu!')
    else:
        print(('Jogada invalida'))
elif machine == 2:
    if player == 2:
        print('Empate!')
    elif player == 0:
        print('Jogador Venceu!')
    elif player == 1:
        print('A máquina venceu!')
    else:
        print(('Jogada invalida'))