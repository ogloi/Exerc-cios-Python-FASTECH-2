total_geral = 0.0

print("=== Cardápio ===")
print("100 - Cachorro Quente  R$ 1,20")
print("101 - Bauru Simples    R$ 1,30")
print("102 - Bauru com ovo    R$ 1,50")
print("103 - Hambúrguer       R$ 1,20")
print("104 - Cheeseburger     R$ 1,30")
print("105 - Refrigerante     R$ 1,00")
print("  0 - Encerrar pedido")

codigo = int(input("Código: "))

while codigo != 0:
    if codigo == 100:
        nome = "Cachorro Quente"
        preco = 1.20
    elif codigo == 101:
        nome = "Bauru Simples"
        preco = 1.30
    elif codigo == 102:
        nome = "Bauru com ovo"
        preco = 1.50
    elif codigo == 103:
        nome = "Hambúrguer"
        preco = 1.20
    elif codigo == 104:
        nome = "Cheeseburger"
        preco = 1.30
    elif codigo == 105:
        nome = "Refrigerante"
        preco = 1.00
    else:
        print("Código inválido!")
        codigo = int(input("Código: "))
        continue

    quantidade = int(input("Quantidade: "))
    subtotal = preco * quantidade
    total_geral += subtotal
    print(f"{nome} x{quantidade} = R$ {subtotal:.2f}")

    codigo = int(input("Código: "))

print(f"Total geral: R$ {total_geral:.2f}")