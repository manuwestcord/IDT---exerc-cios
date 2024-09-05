numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Digite o número da operação desejada: "))

resultado = 0
operacao_valida = True

if operacao == 1:
    resultado = numero1 + numero2

elif operacao == 2:
    resultado = numero1 - numero2

elif operacao == 3:
    resultado = numero1 * numero2

elif operacao == 4:

    if numero2 != 0:
        resultado = numero1 / numero2

    else:
        print("Divisão por zero não é permitida.")
        operacao_valida = False

else:
    print("Operação inválida.")
    operacao_valida = False

if operacao_valida:

    if resultado % 2 == 0:
        paridade = "par"

    else:
        paridade = "ímpar"

    if resultado > 0:
        positividade = "positivo"

    elif resultado < 0:
        positividade = "negativo"

    else:
        positividade = "neutro"

    if resultado == round(resultado):
        tipo = "inteiro"

    else:
        tipo = "decimal"

    print(f"O resultado da operação é {resultado}. Ele é um número {paridade}, {positividade}, e {tipo}.")

