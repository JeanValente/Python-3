'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
total = 0
opcao = ' '
cont_idade = homen = mulher = 0
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        homen += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    total += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break

print(f'Do total de {total} pessoas.')
print(f'Foram registradas {cont_idade} pessoa com mais de 18 anos')
print(f'{homen} homens.')
print(f'{mulher} mulheres com menos de 20 anos.')