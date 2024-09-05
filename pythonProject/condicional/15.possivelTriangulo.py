from xmlrpc.client import boolean

medida1 = float(input("Digite o valor do primeiro lado: "))
medida2 = float(input("Digite o valor do segundo lado: "))
medida3 = float(input("Digite o valor do terceiro lado: "))
somaMedida1e2 = medida1 + medida2
somaMedida2e3 = medida2 + medida3
somaMedida1e3 = medida1 + medida3
possivel = 0

if somaMedida1e3 > medida2 and somaMedida2e3 > medida1 and somaMedida1e2 > medida3:
    possivel = 1

if possivel == 1:
    print("É um triângulo possível!")
    if medida1 == medida2 and medida2 == medida3:
        print("É um triângulo equilátero!")

    elif medida1 == medida2 and medida2 != medida3:
        print("É um triângulo isósceles!")

    elif medida1 == medida3 and medida1 != medida2:
        print("É um triângulo isósceles!")

    elif medida3 == medida2 and medida2 != medida1:
        print("É um triângulo isósceles!")

    elif medida1 != medida2 and medida2 != medida3:
        print("É um triângulo escaleno")

else:
    print("Não é um triângulo possível!")






