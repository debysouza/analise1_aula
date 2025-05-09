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


def exibir_menu():
    print('1-Consultar saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')

def sacar(valor):
    global saldo
    saldo -= valor
    print(f'Saque realizado com sucesso!\nO saldo atual da conta: {saldo}')

def depositar(valor):
    global saldo
    saldo += valor
    print(f'Depósito realizado com sucesso!\nO saldo atual da conta: {saldo}')

def transferir(valor):
    global saldo, destinatario
    saldo -= valor
    destinatario += valor
    print(f'Transferência realizada com sucesso!\nO saldo atual da conta: {saldo}')

while True:
    exibir_menu()
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print(f'O saldo da conta 1: {saldo1}')
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        depositar(valor)
    elif op == 3:
        valor = float(input('Escolha o valor da transferência: '))
        transferir(valor)
    elif op == 4:
        valor = float(input('Escolha o valor do saque: '))
        sacar(valor)
    elif op == 5:
        print('Obrigado!')
        break
    