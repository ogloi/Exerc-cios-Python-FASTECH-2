votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
nulos   = 0
brancos = 0

print("1 - José Alves")
print("2 - Maria Souza")
print("3 - Carlos Lima")
print("4 - Ana Pereira")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar votação")

voto = int(input("Voto: "))

while voto != 0:
    if voto == 1:
        votos_1 += 1
    elif voto == 2:
        votos_2 += 1
    elif voto == 3:
        votos_3 += 1
    elif voto == 4:
        votos_4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Código inválido!")

    voto = int(input("Voto: "))

total = votos_1 + votos_2 + votos_3 + votos_4 + nulos + brancos

print(f"José Alves:   {votos_1} votos")
print(f"Maria Souza:  {votos_2} votos")
print(f"Carlos Lima:  {votos_3} votos")
print(f"Ana Pereira:  {votos_4} votos")
print(f"Nulos:        {nulos} ({nulos/total*100:.1f}%)")
print(f"Brancos:      {brancos} ({brancos/total*100:.1f}%)")