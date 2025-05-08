from conta import ContaCorrente

contas = {
    '1234-5': ContaCorrente('132', '1234-5', 100.0),
    '9876-5': ContaCorrente('111', '9876-5', 2000.0)
}

def login():
    num_conta = input('Digite seu número da conta: ')
    senha = input('Digite sua senha: ')

    conta = contas.get(num_conta)
    if conta and conta.senha == senha:
        print(f'Seja bem-vindo(a), {conta.num_conta}!')
        return conta
    else:
        print('Conta e/ou senha inválida.')
        login()

def exibir_menu():
    print('1-Consultar saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')

conta_logada = login()

while True:
    exibir_menu()
    op = int(input('Escolha uma opção: '))

    if op == 1:
        conta_logada.consultar_saldo()
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        conta_logada.depositar(valor)
    elif op == 3:
        valor = float(input('Escolha o valor da transferência: '))
        num_conta_destino = input('Digite a conta do destinatário: ')
        if num_conta_destino in contas and num_conta_destino != conta_logada.num_conta:
            conta_logada.transferir(contas[num_conta_destino], valor)
        else:
            print('Conta destino não encontrada.')
    elif op == 4:
        valor = float(input('Escolha o valor do saque: '))
        conta_logada.sacar(valor)
    elif op == 5:
        print('Obrigado!')
        break
    else:
        print('Opção inválida. Tente novamente.\n')