menorNumero = int(input("Digite um número: "))
maiorNumero = menorNumero
for x in range (19):
    numeroAtual = int(input("Digite um número: "))

    if numeroAtual < menorNumero:
        menorNumero = numeroAtual

    elif numeroAtual > maiorNumero:
        maiorNumero = numeroAtual

print(f"O menor número é {menorNumero}")
print(f"O maior número é {maiorNumero}")