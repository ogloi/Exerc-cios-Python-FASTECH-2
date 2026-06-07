valor_divida = float(input("Valor da dívida: R$ "))

# parcelas e juros em %
parcelas = [1, 3, 6, 9, 12]
juros    = [0, 10, 15, 20, 25]

print(f"{'Dívida':>12} {'Juros':>8} {'Parcelas':>10} {'Parcela':>12}")
print("-" * 46)

for i in range(5):
    valor_juros = valor_divida * juros[i] / 100
    total       = valor_divida + valor_juros
    valor_parcela = total / parcelas[i]

    print(f"R$ {total:>9.2f} {valor_juros:>8.2f} {parcelas[i]:>10} R$ {valor_parcela:>9.2f}")