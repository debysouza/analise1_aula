def calcular_media(nota1, nota2, nota_optativa):
    if nota_optativa != -1:
        n1, n2 = sorted([nota1, nota2])
        if nota_optativa > n1:
            n1 = nota_optativa
    media = (n1 + n2) / 2
    if media >= 6.0:
        situacao = "Aprovado"
    elif media < 3.0:
        situacao = "Reprovado"
    else:
        situacao = "Exame"
    return media, situacao

nota1 = float(input('Digite a nota da primeira avaliação: '))
nota2 = float(input('Digite a nota da segunda avaliação: '))
nota_optativa = float(input('Digite a nota da avaliação optativa (ou -1 se não fez): '))

media, situacao = calcular_media(nota1, nota2, nota_optativa)

print(f'Média: {media: .2f}')
print(f'Situação: {situacao}')