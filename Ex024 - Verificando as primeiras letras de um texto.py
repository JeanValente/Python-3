'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''

cidade = input('Qual a sua cidade:').strip()
print(cidade[:5].upper() == 'SANTO')

#Quando é para formatar a String, sempre é .alguama coisa ".upper" por exemplo
# Buscar a palavra é []