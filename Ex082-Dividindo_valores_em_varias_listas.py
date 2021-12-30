'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    print('Valor registrado com sucesso.')
    opcao = str(input('Deseja inserir outro número? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Digite [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
par = []
impar = []
for contador, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'A lista inserida tem {len(lista)} números: {lista}')
print(f'{len(par)} desses números são pares: {par}')
print(f'{len(impar)} desses números são ímpares: {impar}')