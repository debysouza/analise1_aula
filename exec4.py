# if/else
def verificar_regiao(codigo):
    if codigo == 1:
        return "Sul"
    elif codigo == 2:
        return "Norte"
    elif codigo == 3:
        return "Leste"
    elif codigo == 4:
        return "Oeste"
    elif codigo == 5 or codigo == 6:
        return "Nordeste"
    elif codigo == 7 or codigo == 8 or codigo == 9:
        return "Sudeste"
    elif codigo == 10:
        return "Centro-Oeste"
    elif codigo == 11:
        return "Noroeste"
    else:
        return "Importado"

codigo_produto = int(input('Digite o código de origem do produto: '))

print(f'Região de procedência: {verificar_regiao(codigo_produto)}')



# match/case
def verificar_regiao(codigo):
    match codigo:
        case 1:
            return "Sul"
        case 2:
            return "Norte"
        case 3:
            return "Leste"
        case 4:
            return "Oeste"
        case 5:
            return "Nordeste"
        case 6:
            return "Nordeste"
        case 7:
            return "Sudeste"
        case 8:
            return "Sudeste"
        case 9:
            return "Sudeste"
        case 10:
            return "Centro-Oeste"
        case 11:
            return "Noroeste"
        case _:
            return "Importado"

codigo_produto = int(input('Digite o código de origem do produto: '))

print(f'Região de procedência: {verificar_regiao(codigo_produto)}')




# match/case reduzido
def verificar_regiao(codigo):
    match codigo:
        case 1:
            return "Sul"
        case 2:
            return "Norte"
        case 3:
            return "Leste"
        case 4:
            return "Oeste"
        case _ if 5 <= codigo <= 6:
            return "Nordeste"
        case _ if 7 <= codigo <= 9:
            return "Sudeste"
        case 10:
            return "Centro-Oeste"
        case 11:
            return "Noroeste"
        case _:
            return "Importado"

codigo_produto = int(input('Digite o código de origem do produto: '))

print(f'Região de procedência: {verificar_regiao(codigo_produto)}')





# dicionario
def verificar_regiao(codigo):
    return {
        1: "Sul",
        2: "Norte",
        3: "Leste",
        4: "Oeste",
        5: "Nordeste",
        6: "Nordeste",
        7: "Sudeste",
        8: "Sudeste",
        9: "Sudeste",
        10: "Centro-Oeste",
        11: "Noroeste"
    }.get(codigo, "Importado")

codigo_produto = int(input('Digite o código de origem do produto: '))

print(f'Região de procedência: {verificar_regiao(codigo_produto)}')




# dicionario reduzido
def verificar_regiao(codigo):
    return {
        1: "Sul",
        2: "Norte",
        3: "Leste",
        4: "Oeste",
        **{codigo: "Nordeste" for codigo in range(5, 6)},
        **{codigo: "Sudeste" for codigo in range(7, 9)},
        10: "Centro-Oeste",
        11: "Noroeste"
    }.get(codigo, "Importado")

codigo_produto = int(input('Digite o código de origem do produto: '))

print(f'Região de procedência: {verificar_regiao(codigo_produto)}')