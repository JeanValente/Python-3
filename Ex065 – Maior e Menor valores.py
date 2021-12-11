'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
contador = soma = menor = maior = 0
opcao = 'S'
while opcao == 'S':
    numero = int(input('Valor: '))
    opcao = input('Deseja continuar? [S/N]').upper().strip()[0]
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / contador

print('Foram digitados {} valores. A media foi de {}, o maior numero foi {} e o menor foi {}.'.format(contador, media, maior, menor))
