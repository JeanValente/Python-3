'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


from random import randint
num2 = 0

computador = (randint(0, 10))
print('''Olá humano, gostaria de jogar um jogo?
Acabei de pensar em um número de 0 a 10.
Sabe me dizer qual foi ''')
acertou = False
chances = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    chances += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo')
        elif jogador > computador:
            print('Menos... Tente de novo')

print('Você acertou! Precisou de {} chances para me vencer'.format(chances))
