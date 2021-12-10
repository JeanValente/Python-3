'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

# import random (do random só vou usar o shuffle)
from random import shuffle
n1 = input('Primeiro aluno:')
n2 = input('Terceiro aluno')
n3 = input('Segundo aluno')
n4 = input('Quarto aluno')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
