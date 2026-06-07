n = int(input("Linhas: "))
m = int(input("Colunas: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# cria a transposta (m linhas, n colunas)
transposta = []
for j in range(m):
    nova_linha = []
    for i in range(n):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

print("Matriz transposta:")
for linha in transposta:
    print(linha)