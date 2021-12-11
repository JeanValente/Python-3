'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

preco = float(input('Valor do produto: R$'))
print('''Condições de pagamento:
[1] À vista dinheiro/cheque: 10% de desconto
[2] Débito: 5% de desconto
[3] Até 2x no cartão
[4] 3x ou mai no cartão: 20% de juros''')
condicao = int(input('Opção:'))

dez = preco - ((preco * 10)/100)
cinco = preco - ((preco * 5)/100)
vinte = preco + ((preco * 20)/100)

print('Valor final: R$ ', end='')
if condicao == 1:
    print('{:.2f} à vista '.format(dez))
elif condicao == 2:
    print('{:.2f} no débito'.format(cinco))
elif condicao == 3:
    print('{:.2f} em até 2x de R${:.2f}'.format(preco, preco / 2))
elif condicao == 4:
    print('{:.2f} em 3x ou mais'.format(vinte))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE')