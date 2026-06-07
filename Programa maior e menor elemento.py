n = int(input("Linhas: "))
m = int(input("Colunas: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        valor = float(input(f"  Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(n):
    for j in range(m):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")