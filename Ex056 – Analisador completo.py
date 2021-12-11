'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
 e quantas mulheres têm menos de 20 anos.'''
soma_idade = 0
media_idade = 0
maior_homen = 0
nome_velho = ''
mulher_20 = 0
print('=' * 6, 'ANALISADOR COMPLETO', '=' * 6)
for p in range(1, 5):
    print('=' * 17)
    print('   {}ª pessoa'.format(p))
    print('=' * 17)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_homen = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_homen:
        maior_homen = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_20 += 1

media_idade = soma_idade / 4

print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homen mais velho tem {} anos e se chama {}'.format(maior_homen, nome_velho))
print('Ao todo, são {} mulheres com menos de 20 anos'.format(mulher_20))



