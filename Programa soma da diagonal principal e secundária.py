n = int(input("Tamanho N da matriz NxN: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = float(input(f"  Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma_principal  = 0.0
soma_secundaria = 0.0

for i in range(n):
    soma_principal  += matriz[i][i]
    soma_secundaria += matriz[i][n - 1 - i]

print(f"Soma diagonal principal: {soma_principal}")
print(f"Soma diagonal secundária: {soma_secundaria}")