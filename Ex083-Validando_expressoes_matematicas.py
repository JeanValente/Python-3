'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''


expressao = str(input('Digite a expressão: '))
lista = list(expressao)
if lista[0] == ')':
    print('A expressão está errada!')
else:
    d = lista.count('(')
    e = lista.count(')')
    if d == e:
        print('A expressão está correta!')
    else:
        print('E espressão está errada!')


