conta_0_25  = 0
conta_26_50 = 0
conta_51_75 = 0
conta_76_100 = 0

numero = float(input("Digite um número (negativo para encerrar): "))

while numero >= 0:
    if numero <= 25:
        conta_0_25 += 1
    elif numero <= 50:
        conta_26_50 += 1
    elif numero <= 75:
        conta_51_75 += 1
    elif numero <= 100:
        conta_76_100 += 1

    numero = float(input("Digite um número (negativo para encerrar): "))

print("Intervalo [0-25]:", conta_0_25)
print("Intervalo [26-50]:", conta_26_50)
print("Intervalo [51-75]:", conta_51_75)
print("Intervalo [76-100]:", conta_76_100)