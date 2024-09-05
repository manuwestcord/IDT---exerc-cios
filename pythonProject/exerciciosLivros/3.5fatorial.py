numeroN = int(input("Digite um número: "))
fatorial = 1

for x in range(numeroN, 0, -1):
    fatorial *= x


print(fatorial)