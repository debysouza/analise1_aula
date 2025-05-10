# try:
#     # Código que pode dar erro
# except:
#     # Código executado se houver erro (pode ter várias exceções diferentes)
# else:
#     # Código executado se NÃO houver erro (opcional)
# finally:
#     # Código executado sempre (opcional)

def soma(a, b):
    if a % 2 != 0 or b % 2 != 0:
        raise ValueError('Um dos valores é ímpar')
    if a < 0 or b < 0:
        raise ValueError('Não aceita valores negativos')
    return a+b

#print(soma(5, 2))

try:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    resultado = soma(a, b)
except ValueError as ve:
    print('Erro: ', ve)
except Exception as e:
    print('Erro inesperado! ', e)
else:
    print('Soma = ', resultado)
finally:
    print('Fim do par!')
