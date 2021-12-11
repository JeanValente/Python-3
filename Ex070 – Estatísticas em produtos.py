'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = caro = menor = contador = 0
barato = ' '
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        caro += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar: ').upper().strip()[0]
    if opcao == 'N':
        break

print(f'Total da compra: R${total:.2f} ')
print(f'{caro} produtos acima de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')