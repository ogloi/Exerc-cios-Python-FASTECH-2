n = int(input("Valor de N: "))

H = 0.0
for i in range(1, n + 1):
    H += 1 / i

print(f"H com {n} termos = {H:.6f}")