valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    print("O primeiro produto que deve ser comprado")

elif valor2 < valor1 and valor2 < valor3:
    print("O segundo produto que deve ser comprado")

elif valor3 < valor2 and valor3 < valor2:
    print("O terceiro produto que deve ser comprado")

elif valor1 == valor2 or valor2 == valor3 or valor1 == valor3:
    print("Os dois produtos mais baratos tem o mesmo valor")