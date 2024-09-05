altura = float(input("Digite a sua altura: "))
sexo = (input("Digite M se for vc for sexo masculino e F para feminino: "))

if sexo == "M":
    pesoIdeal = (72.7 * altura) - 58

else:
    pesoIdeal = (62.1 * altura) - 44.7

print(f"O seu peso ideal é: {pesoIdeal:.2f}")