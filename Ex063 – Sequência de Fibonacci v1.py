'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8'''

print('-' * 20)
print('Sequência Fibonacci')
print('-' * 20)
numero = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} > {}'.format(t1, t2), end='')
contador = 3
while contador <= numero:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' > Fim')
print('~'*30)