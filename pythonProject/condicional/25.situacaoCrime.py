respostasPositivas = 0

resposta1 = input("Telefonou para a vítima? (sim/não): ")
if resposta1 == "sim":
    respostasPositivas += 1

resposta2 = input("Esteve no local do crime? (sim/não): ")
if resposta2 == "sim":
    respostasPositivas += 1

resposta3 = input("Mora perto da vítima? (sim/não): ")
if resposta3 == "sim":
    respostasPositivas += 1

resposta4 = input("Devia para a vítima? (sim/não): ")
if resposta4 == "sim":
    respostasPositivas += 1

resposta5 = input("Já trabalhou com a vítima? (sim/não): ")
if resposta5 == "sim":
    respostasPositivas += 1


if respostasPositivas == 2:
    classificacao = "Suspeita"
elif respostasPositivas >= 3 and respostasPositivas <= 4:
    classificacao = "Cúmplice"
elif respostasPositivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("Classificação:", classificacao)
