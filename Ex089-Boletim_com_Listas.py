'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2)/2
    ficha.append([nome, [nota_1, nota_2], media])
    opcao = input('Deseja inserir outro aluno? [S/N}: ').strip().upper()[0]
    if opcao in 'N':
        break
print('=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('=' * 35)
    sem = int(input('Notas por semestre: No. do aluno "999 interrompe": '))
    if sem == 999:
        print('Finalizando.')
        break
    if sem <= len(ficha) - 1:
        print(f'Notas de {ficha[sem][0]} são {ficha[sem][1]}')


