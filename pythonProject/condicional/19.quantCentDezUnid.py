numero = int(input("Digite um número de 0 à 1000: "))

if numero < 0 or numero >= 1000:
    print("Número inválido")

else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    if centenas > 0:
        print(f"{centenas} centenas")

    if dezenas > 0:
        print(f"{dezenas} dezenas")

    if unidades > 0:
        print(f"{unidades} unidades")

