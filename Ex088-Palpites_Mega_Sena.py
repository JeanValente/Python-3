'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
 tudo em uma lista composta.'''

from random import randint
aposta = []
lista_de_apostas = []

print('=' * 30)
print('         MEGA DA VIRADA      ')
print('=' * 30)
quant = int(input('Quantos jogos quer sortear?: '))
total = 1
while total <= quant:
    cont = 0
    while True:
            num = randint(1, 60)
            if num not in aposta:
                aposta.append(num)
                cont += 1
            if cont >= 6:
                break
    aposta.sort()
    lista_de_apostas.append(aposta[:])
    aposta.clear()
    total += 1

print('='* 3, f'SORTEANDO {quant} JOGOS', '=' * 3)
for indice, lista in enumerate(lista_de_apostas):
    print(f'JOGO {indice + 1}: {lista}')
