# 1- Criar lógica que verifica o saldo de
# uma conta corrente.
# - conta1, saldo

# 2- Criar uma segunda conta corrente, para simular
# saque, depósito e transferência.
# - conta2, saldo
# - saque, depósito e transferência

# 3- Criar um menu que permite ao usuário realizar N
# transações até que ele opte por sair.
# - utilizar while com menu

conta1 = '1234'
saldo1 = 100.0

conta2 = '7894'
saldo2 = 2000.0

while True:
    print('1-Consultar saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print(f'O saldo da conta 1: {saldo1}')
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        saldo1 += valor
        print(f'Depósito realizado com sucesso!\nO saldo atual da conta 1: {saldo1}')
    elif op == 3:
        valor = float(input('Escolha o valor da transferência: '))
        saldo1 -= valor
        saldo2 += valor
        print(f'Transferência realizada com sucesso!\nO saldo atual da conta 1: {saldo1}')
    elif op == 4:
        valor = float(input('Escolha o valor do saque: '))
        saldo1 -= valor
        print(f'Saque realizado com sucesso!\nO saldo atual da conta 1: {saldo1}')
    elif op == 5:
        print('Obrigado!')
        break







    # match op:
    #     case 1:
    #         print(f'O saldo da conta 1: {saldo1}')
    #     case 2:
    #         valor = float(input('Escolha o valor do depósito: '))
    #         saldo1 += valor
    #         print(f'Depósito realizado com sucesso!\nO saldo atual da conta 1: {saldo1}')
    #     case 3:
    #         valor = float(input('Escolha o valor da transferência: '))
    #         saldo1 -= valor
    #         saldo2 += valor
    #         print(f'Transferência realizada com sucesso!\nO saldo atual da conta 1: {saldo1}')
    #     case 4:
    #         valor = float(input('Escolha o valor do saque: '))
    #         saldo1 -= valor
    #         print(f'Saque realizado com sucesso!\nO saldo atual da conta 1: {saldo1}')
    #     case 5:
    #         print('Obrigado!')
    #         break

# Critérios de diferença entre if/else e match/case
## Compatibilidade ampla - if/else
## Condições complexas - if/else
## Código mais organizado - match/case
## Ideal para menus de opções - if/else e match/case
