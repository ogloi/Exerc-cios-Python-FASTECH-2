n = int(input("Quantos termos? "))

soma = 0.0
denominador = 1

for numerador in range(1, n + 1):
    termo = numerador / denominador
    print(f"  {numerador}/{denominador} = {termo:.4f}")
    soma += termo
    denominador += 2

print(f"Soma da série com {n} termos: {soma:.4f}")