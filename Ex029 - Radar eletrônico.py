'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Velocidade marcada:'))

if velocidade > 80:
    print('Você ultrapassou o limite de 80Km/h')
    print('Multa de R${:.2f}'.format((velocidade - 80)*7))

print('Tenha um bom dia! Dirija com segurança!')



