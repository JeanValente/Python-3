''' Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = int(input('Primeiro valor:'))
b = int(input('Segundo Valor:'))
c = int(input('Terceiro Valor:'))

#Verificnado quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor foi {} '.format(menor))
print("O maior valor foi {}".format(maior))
