'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

color = {'blue':'\033[7;34m', 'red':'\033[7;31m', 'yelow':'\033[7;33m', 'green':'\033[7;32m', 'purple':'\033[7;35m', 'cleam':'\033[m'}

nota_1 = float(input('Nota primeiro semestre: '))
nota_2 = float(input('Nota segundo semestre: '))
media = (nota_1 + nota_2) / 2

if media < 5:
    print('A sua média final foi {}. Você foi {}REPROVADO!{}'.format(media, cores['red'], cores['cleam']))
elif media > 5.0 and media < 7.0:
    print(' A sua média final foi {}. Você esta de {}RECUPERAÇÃO!{}'.format(media, cores['yelow'], cores['cleam']))
elif media >= 7.0:
    print('A sua média final foi {}. Você foi {}APROVADO!{}'.format(media, cores['green'], cores['cleam']))

# elif 7 < media > 5.0 : também da certo