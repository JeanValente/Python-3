


'''co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual é o cumprimento do cateto adjacente?'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual é o cumprimento do cateto adjacente?'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))