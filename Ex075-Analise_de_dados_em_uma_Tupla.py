'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('1º numero: ')), int(input('2º numero: ')), int(input('3º numero: ')), int(input('4º numero: ')))
print(f'O número 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3)+ 1}ª posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares foram:')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

