import math

def calcular_lampadas(potencia, largura, comprimento):
    area = largura * comprimento
    potencia_necessaria = 3 * area
    num_lampadas = math.ceil(potencia_necessaria / potencia)
    num_bocais = math.ceil(area / 3)

    print(f'Número de lâmpadas necessárias: {int(num_lampadas)}')
    print(f'Número de bocais necessários: {int(num_bocais)}')

potencia = float(input('Digite a potência da lâmpada (em wats): '))
largura = float(input('Digite a largura do cômodo (em metros): '))
comprimento = float(input('Digite o comprimento do cômodo (em metros): '))

calcular_lampadas(potencia, largura, comprimento)