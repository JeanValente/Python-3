dia = int(input('Dias usados:'))
km = float(input('Km rodados:'))
total = (dia*60)+(km * 0.15)
print('O total a pagar é de R${:.2f}'. format(total))