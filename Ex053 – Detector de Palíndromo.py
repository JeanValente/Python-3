'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

'''frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso = ''
for letra in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[letra]
print('O inverso de {} é {}'.format(tudo_junto, inverso))
if inverso == tudo_junto:
    print('a frase é um PALÍMDROMO!')
else:
    print('A frase NÃO é um PALÍNDROMO.')'''
# Fazer o exercicio sem on for

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso = tudo_junto[::-1]

print('O inverso de {} é {}'.format(tudo_junto, inverso))
if inverso == tudo_junto:
    print('a frase é um PALÍMDROMO!')
else:
    print('A frase NÃO é um PALÍNDROMO.')
