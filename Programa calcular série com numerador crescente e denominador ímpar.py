n = int(input("Quantos termos? "))

soma = 0.0
denominador = 1

for numerador in range(1, n + 1):
    soma += numerador / denominador
    denominador += 2

print(f"Soma com {n} termos: {soma:.4f}")