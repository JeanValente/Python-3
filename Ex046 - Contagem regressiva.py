'''Exercício 46 - Crie uma contagem regressiva de 10 até 1'''

from time import sleep
executavel = input('APERTE ENTER PARA INICIAR O LANCAMENTO')
sleep(1.5)
print('INICIANDO...')
sleep(2)
print('PREPARAR PARA DECOLAR...')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('DECOLAR!')


