'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Digite [S/N]: ')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Os número em ordem decrescente são :{lista})
if 5 not in lista:
    print('O número 5 não esta na lista')
else:
    print('O numero 5 está na lista')

