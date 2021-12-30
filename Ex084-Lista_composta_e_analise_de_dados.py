'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Digite [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break


print('-' * 40)

print(f'Foram registradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()