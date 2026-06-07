n = int(input("Número de linhas: "))

matriz = []
for i in range(n):
    linha = []
    qtd_colunas = int(input(f"Quantas colunas na linha {i+1}? "))
    for j in range(qtd_colunas):
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# verifica se todas as linhas têm o mesmo número de colunas
colunas_primeira = len(matriz[0])
regular = True

for i in range(1, n):
    if len(matriz[i]) != colunas_primeira:
        regular = False

quadrada = (n == colunas_primeira) and regular

print(f"Quadrada: {quadrada}")
print(f"Regular: {regular}")