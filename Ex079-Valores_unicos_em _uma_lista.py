'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado')
    else:
        print('Numero duplicado, não vou inserir')
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'NS':
        opcao = str(input('Digite [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break

print(f'Os número digitado em ordem crescente são: {sorted(lista)}')


