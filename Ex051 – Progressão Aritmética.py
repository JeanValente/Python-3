'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

print('=' * 17)
print('TERMOS DE UMA PA')
print('=' * 17)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'. format(c), end=' > ')
print('FIM')