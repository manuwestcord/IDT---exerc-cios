import math

valorA = int(input("Digite um valor A: "))
valorB = int(input("Digite um valor B: "))
valorC = int(input("Digite um valor C: "))

delta = valorB ** 2 - 4 * valorA * valorC
xLinha = ((-valorB) + math.sqrt(delta))/ 2 * valorA
xBiLinha = ((-valorB) - math.sqrt(delta))/ 2 * valorA

print("x' = ", xLinha)
print("x'' = ", xBiLinha )

#Para determinar raízes tem que ser valores que fechem a raíz exata, exemplo para teste de mesa:
# A = 1; B = -2; C = 1