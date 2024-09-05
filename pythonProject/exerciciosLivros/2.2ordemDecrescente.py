numero1 = (input("Digite o primeiro valor: "))
numero2 = (input("Digite o segundo valor: "))
numero3 = (input("Digite o terceiro valor: "))

if numero1 < numero2 and numero2 < numero3:
    print(numero1, ", ", numero2, ", ", numero3 )

if numero1 < numero3 and numero3 < numero2:
    print(numero1, ", ", numero3, ", ", numero2)

if numero2 < numero1 and numero1 < numero3:
    print(numero2, ", ", numero1, ", ", numero3)

if numero2 < numero3 and numero3 < numero1:
    print(numero2, ", ", numero3, ", ", numero1)

if numero3 < numero2 and numero2 < numero1:
    print(numero3, ", ", numero2, ", ", numero1)

if numero3 < numero1 and numero1 < numero2:
    print(numero3, ", ", numero1, ", ", numero2)