valorSaque = int(input("Digite o valor do saque: "))

if valorSaque < 10 or valorSaque > 600:
    print("Valor inválido")

else:
    notas100 = 0
    notas50 = 0
    notas10 = 0
    notas5 = 0
    notas1 = 0

    while valorSaque >= 100:
        notas100 += 1
        valorSaque -= 100

    while valorSaque >= 50:
        notas50 += 1
        valorSaque -= 50

    while valorSaque >= 10:
        notas10 += 1
        valorSaque -= 10

    while valorSaque >= 5:
        notas5 += 1
        valorSaque -= 5

    while valorSaque >= 1:
        notas1 += 1
        valorSaque -= 1

    print("O saque vai ser feito em:")
    if notas100 > 0:
        print(f"{notas100} notas de 100 reais")
    if notas50 > 0:
        print(f"{notas50} notas de 50 reais")
    if notas10 > 0:
        print(f"{notas10} notas de 10 reais")
    if notas5 > 0:
        print(f"{notas5} notas de 5 reais")
    if notas1 > 0:
        print(f"{notas1} notas de 1 real")