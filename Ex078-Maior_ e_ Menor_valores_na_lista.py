'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = []
for contador in range(0, 5):
    valores.append(int(input(f'Digite o {contador + 1}º Valor: ')))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os números : {valores}')
print(f'O maior valor é {maior} e esta na(s) posição(es) ', end=' ')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao}...', end='')
print(f'\nO menor número é {menor} e está na(s) posição(es) ', end=' ')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao}...', end='')
print()
