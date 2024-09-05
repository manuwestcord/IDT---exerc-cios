posicao = int(input("Digite o valor da posição que deseja para a série de Fibonacci: "))
termoAnterior = 0
numero = 1


for x in range(posicao):
    print(numero, end=" ")
    numero = numero + termoAnterior
    termoAnterior = numero - termoAnterior
