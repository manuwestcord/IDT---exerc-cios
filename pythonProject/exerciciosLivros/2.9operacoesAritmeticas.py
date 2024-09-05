valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = int(input("Digite a operação aritmética\n 1- Soma\n 2- Subtração\n 3- Multiplicação\n 4- Divisão: "))
resultado = 0

if operacao == 1:
    resultado = (valor1 + valor2)
    print(resultado)

elif operacao == 2:
    resultado = (valor1 - valor2)
    print(resultado)

elif operacao == 3:
    resultado = (valor1 * valor2)
    print(resultado)

elif operacao == 4:
    resultado = (valor1 / valor2)
    print(resultado)

else:
    print("Operação inválida")