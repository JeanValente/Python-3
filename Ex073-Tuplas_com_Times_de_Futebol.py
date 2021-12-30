'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport Recife', 'Chapecoense')
print('-' * 55)
print(times)
print('-' * 55)
print(f'Os classificado para a Copa Libertadores são {times[0:5]}')
print('-' * 55)
print(f'Os quatro times rebaixados foram {times[-4:]}')
print('-' * 55)
print(f'Os times em ordem afabética são {sorted(times)}')
print('-' * 55)
print(f'A Chapecoense ficou em {times.index("Chapecoense")+ 1}º lugar')