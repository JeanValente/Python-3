larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg*alt
tint = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.3f}l de tinta'.format(tint))