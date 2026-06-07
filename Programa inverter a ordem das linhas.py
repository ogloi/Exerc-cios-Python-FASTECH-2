n = int(input("Linhas: "))
m = int(input("Colunas: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

invertida = []
for i in range(n - 1, -1, -1):
    invertida.append(matriz[i])

print("Matriz com linhas invertidas:")
for i in range(n):
    print(invertida[i])