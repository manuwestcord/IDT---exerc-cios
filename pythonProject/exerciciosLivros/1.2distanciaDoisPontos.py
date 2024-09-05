import math

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1) **2)

print("A distância entre esses dois pontos é dAB = ", distancia )

#O exemplo utilizado para o teste de mesa foi x1 = 1; y1 = 1; x2 = 1; y2 = 4