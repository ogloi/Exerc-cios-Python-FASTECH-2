texto = input("Digite uma string: ")

invertido = ""
for i in range(len(texto) - 1, -1, -1):
    invertido = invertido + texto[i]

print(f"Invertida: {invertido}")