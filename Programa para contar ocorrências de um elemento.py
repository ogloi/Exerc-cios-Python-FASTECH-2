n = int(input("Linhas: "))
m = int(input("Colunas: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

elemento = int(input("Elemento a buscar: "))
contador = 0

for i in range(n):
    for j in range(m):
        if matriz[i][j] == elemento:
            contador += 1

print(f"O elemento {elemento} aparece {contador} vez(es).")