somaNotas = 0
for x in range (5):
    nota = float(input(f"Digite a {x + 1} ª nota: "))
    notaPonderada = nota * (x + 1)
    somaNotas += notaPonderada

mediaPonderada = somaNotas / 15
print(mediaPonderada)
