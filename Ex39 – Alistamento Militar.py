'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Você tem {} anos. Você deve se alistar IMEDIATAMENTE!'.format(idade))
elif idade > 18:
    print('Você tem {} anos. Seu alistamento foi em {}. Você esta {} anos atrasado'.format(idade, ano + 18, idade - 18))
elif idade < 18:
    print('Você tem {} anos. Seu alistamento será em {}'.format(idade, ano + 18))

