'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

resposta = ' '
while resposta != 'N':
    numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
              'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    resposta = ' '
    while True:
        entrada = int(input('Digite um número entre 0 e 20: '))
        if 0 <= entrada <= 20:
            break
        print('Tente novamente', end='')
    print(f'O número digitado foi {numero[entrada]}')
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
print('Até mais')