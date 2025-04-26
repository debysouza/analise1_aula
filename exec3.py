def calcular_rendimento(odometro_inicio, odometro_fim, litros, valor):
    km_rodados = odometro_fim - odometro_inicio
    media_consumo = km_rodados / litros
    lucro = valor - (litros * 4.87)

    print(f'Média de consumo: {media_consumo: .2f} km/L')
    print(f'Lucro do dia: R$ {lucro: .2f}')

odometro_inicio = float(input('Digite a marcação do odômetro no início do dia (km): '))
odometro_fim = float(input('Digite a marcação do odômetro no final do dia (km): '))
litros = float(input('Digite o número de litros de combustível gasto: '))
valor = float(input('Digite o valor total recebido dos passageiros: R$ '))

calcular_rendimento(odometro_inicio, odometro_fim, litros, valor)