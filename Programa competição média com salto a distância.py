nome = input("Nome do atleta (Enter para sair): ")

while nome != "":
    saltos = []

    for i in range(1, 6):
        distancia = float(input(f"  {i}º salto (m): "))
        saltos.append(distancia)

    # encontra melhor e pior
    melhor = saltos[0]
    pior   = saltos[0]
    for i in range(1, 5):
        if saltos[i] > melhor:
            melhor = saltos[i]
        if saltos[i] < pior:
            pior = saltos[i]

    # soma os 3 do meio (ignora melhor e pior cada vez)
    ja_removeu_melhor = False
    ja_removeu_pior   = False
    soma = 0.0

    for i in range(5):
        if saltos[i] == melhor and not ja_removeu_melhor:
            ja_removeu_melhor = True
        elif saltos[i] == pior and not ja_removeu_pior:
            ja_removeu_pior = True
        else:
            soma += saltos[i]

    media = soma / 3

    print(f"  Melhor: {melhor}m | Pior: {pior}m | Média: {media:.2f}m")
    print(f"Resultado: {nome}: {media:.2f}m")

    nome = input("Nome do atleta (Enter para sair): ")