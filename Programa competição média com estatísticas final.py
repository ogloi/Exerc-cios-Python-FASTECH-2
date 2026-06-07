nome = input("Nome do ginasta: ")
notas = []

for i in range(7):
    nota = float(input(f"  Nota {i+1}: "))
    notas.append(nota)

# encontra melhor e pior
melhor = notas[0]
pior   = notas[0]
for i in range(1, 7):
    if notas[i] > melhor:
        melhor = notas[i]
    if notas[i] < pior:
        pior = notas[i]

# soma as 5 restantes
ja_removeu_melhor = False
ja_removeu_pior   = False
soma = 0.0

for i in range(7):
    if notas[i] == melhor and not ja_removeu_melhor:
        ja_removeu_melhor = True
    elif notas[i] == pior and not ja_removeu_pior:
        ja_removeu_pior = True
    else:
        soma += notas[i]

media = soma / 5

print(f"Atleta: {nome}")
print(f"Melhor nota: {melhor}")
print(f"Pior nota: {pior}")
print(f"Média: {media:.2f}")