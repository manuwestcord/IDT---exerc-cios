inteiro1 = int(input("Digite um número inteiro: "))
inteiro2 = int(input("Digite mais um número inteiro: "))
real = float(input("Agora digite um valor real (com casas decimais): "))

produto = (inteiro1 * 2) * (inteiro2 / 2)
soma = (inteiro1 * 3) + real
potencia = real ** 3

print("O produto do dobro do primeiro com metade do segundo é igual a: ", produto,
      ", a soma do triplo do primeiro com o terceiro é igual a: ", soma,
      "e o terceiro elevado ao cubo é igual a: ", potencia)