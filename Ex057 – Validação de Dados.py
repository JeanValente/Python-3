'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite qual sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'MASCULINO'
else:
   sexo = 'FEMININO'
print('Sexo {} registrado!'.format(sexo))