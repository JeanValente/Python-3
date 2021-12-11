''' Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
 consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('-' * 20)
print('Par ou Ímpar')
print('-' * 20)
wins = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    soma = computador + jogador
    aposta = ' '
    while aposta not in 'PI':
        aposta = str(input('Par ou ìmpar? [P/I] ').upper().strip()[0])
    print(f'Jogador jogou {jogador} e computador jogou {computador}. O total foi {soma}. ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if aposta == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            wins += 1
        else:
            print('Computador Venceu!')
            break
    elif aposta == 'I':
        if soma % 2 == 1:
            print('Você venceu')
            wins += 1
        else:
            print('Computador Venceu!')
            break
    print('Vamos jogar novamente')

print(f'Fim de jogo, o jogador teve {wins} vitória(s) consecutiva(s)')



