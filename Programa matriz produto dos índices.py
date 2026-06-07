n = int(input("Linhas: "))
m = int(input("Colunas: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(i * j)
    matriz.append(linha)

print("Matriz i * j:")
for i in range(n):
    print(matriz[i])