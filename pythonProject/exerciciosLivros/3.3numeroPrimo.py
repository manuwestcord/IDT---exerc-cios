numero = int(input("Digite um número: "))
cont = 0

for x in range (1, numero + 1):
    if numero % x == 0:
        cont += 1
if cont == 2:
    print("É um número primo")

else:
    print("Não é primo")
