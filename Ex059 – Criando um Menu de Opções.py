''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
opcao = 0
sair = False

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print(' {} + {} = {} '.format(num1, num2, (num1 + num2)))
    elif opcao == 2:
        print('{} x {} = {}'.format(num1, num2, (num1 * num2)))
    elif opcao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        else:
            print('{} é maior que {}'.format(num2, num1))
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Fim')

    else:
        print('Opção invalida. Tente novamente')
    print('=' * 30)
    sleep(2)
print('Fim')