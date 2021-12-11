# Meu projeto de caixa eletrônico

from time import sleep
print('=' * 30)
print('{:^30}'.format('BANCO BATEIAS'))
print('=' * 30)
saldo = 1000
senha = ' '
while senha != 'Admin':
    senha = str(input('Digite a sua senha: ')).strip()

opcao = 0
while opcao != 3:
    sleep(2)
    print('''   MENU 
    [1] Saldo
    [2] Saque
    [3] Sair''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print(f'Seu saldo é de R${saldo:.2f}')
    if opcao == 2:
        saque = int(input('Digite o valor: R$ '))
        if saldo >= saque:
            print('Saque aprovado')
            sleep(1)
            print('Contando...')
            sleep(2)
            saldo = saldo - saque
            total = saque
            ced = 50
            total_ced = 0
            while True:
                if saque >= ced:
                    saque -= ced
                    total_ced += 1
                else:
                    if total_ced > 0:
                        print(f'Total de {total_ced} cédulas de R${ced}')
                    if ced == 50:
                        ced = 20
                    elif ced == 20:
                        ced = 10
                    elif ced == 10:
                        ced = 1
                    total_ced = 0
                    if saque == 0:
                        break
        else:
            print('Saldo insuficiente')
sleep(1)
print('Obrigado e volte sempre')
sleep(1)
print('=' * 30)
print('{:^30}'.format('BANCO BATEIAS'))
print('=' * 30)