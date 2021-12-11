'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('=' * 17)
print('TERMOS DE UMA PA')
print('=' * 17)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão dinalizada com {} termos mostrados'.format(total))
print('Fim')
