import math

def calcular_azulejos(comprimento, largura, altura):
    area_parede = 2 * altura * (comprimento + largura)
    caixas_azulejos = area_parede / 1.5
    print (f'Quantidade de caixas de azulejos necessárias: {math.ceil(caixas_azulejos)}')

comprimento = float(input('Digite o comprimento da cozinha (em metros): '))
largura = float(input('Digite a largura da cozinha (em metros): '))
altura = float(input('Digite a altura das paredes da cozinha (em metros): '))

calcular_azulejos(comprimento, largura, altura)