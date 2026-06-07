texto = input("Digite uma string: ").lower()

vogais     = "aeiou"
qtd_vogais = 0
qtd_consoantes = 0

for i in range(len(texto)):
    letra = texto[i]
    if letra >= "a" and letra <= "z":   # é letra
        if letra in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

print(f"Vogais: {qtd_vogais}")
print(f"Consoantes: {qtd_consoantes}")