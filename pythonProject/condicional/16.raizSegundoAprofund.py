import math

valorA = float(input("Digite o valor de A: "))

if valorA != 0:
    valorB = float(input("Digite o valor de B: "))
    valorC = float(input("Digite o valor de C: "))

    delta = valorB ** 2 - 4 * valorA * valorC
    xLinha = ((-valorB) + math.sqrt(delta))/ 2 * valorA
    xBiLinha = ((-valorB) - math.sqrt(delta))/ 2 * valorA
    raizDeltaNulo = ((-valorB)/ 2 * valorA)

    if delta < 0:
        print("O delta é negativo, ou seja, não há raízes existentes, encerrando o programa.")

    elif delta == 0:
        print("O delta é nulo, ou seja, só tem uma raiz. A raiz é igual a ", raizDeltaNulo)

    elif delta > 0:
        print("As raízes são: x' = ", xLinha, " x'' = ", xBiLinha )



