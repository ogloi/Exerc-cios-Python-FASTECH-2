gabarito = ["A","B","C","D","E","E","D","C","B","A"]

total_alunos = 0
soma_notas   = 0
maior_acerto = 0
menor_acerto = 10

continuar = "s"

while continuar == "s":
    acertos = 0

    for i in range(10):
        resposta = input(f"Questão {i+1}: ").upper()
        if resposta == gabarito[i]:
            acertos += 1

    print(f"Acertos: {acertos}/10  Nota: {acertos:.1f}")

    total_alunos += 1
    soma_notas   += acertos

    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos

    continuar = input("Outro aluno? (s/n): ").lower()

media = soma_notas / total_alunos
print(f"Maior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos: {total_alunos}")
print(f"Média da turma: {media:.2f}")