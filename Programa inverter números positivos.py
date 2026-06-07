numero = input("Digite um número inteiro positivo: ")

invertido = ""
for i in range(len(numero) - 1, -1, -1):
    invertido = invertido + numero[i]

print(f"Invertido: {invertido}")