nome = input('Digite seu nome completo:')
maiúscula = nome.upper()
mínusculas = nome.lower()
quant = len(nome)
divido = nome.split()
primeiro_nome = divido[0]
primeiro = len(primeiro_nome)


print('Seu nome em maiúculas é {}'.format(maiúscula))
print('Seu nome em minúsculas é {}'.format(mínusculas))
print('Seu nome tem ao todo {} letras'.format(quant))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome, primeiro))


