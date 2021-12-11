'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))

prestação = valor_casa / (anos * 12)
total_pago = (salário * 30 / 100) * (anos * 12)
entrada = valor_casa - total_pago
print('Para pagar a casa no valor de R${:.2f} em {} anos.'.format(valor_casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))


if prestação >= salário * 30 / 100:
    print('Empréstimo {}NEGADO.{}'.format('\033[41m', '\033[m'))
    print('Entrada nescesária: R${:.2f}'.format(entrada))
else:
    print('Empréstimo {}APROVADO!{}'.format('\033[42m', '\033[m'))


