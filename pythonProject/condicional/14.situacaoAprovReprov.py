from multiprocessing.managers import Array

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
conceito = ""

if media <= 10 and media >= 9:
    conceito = "A"

elif media < 9 and media >= 7.5:
    conceito = "B"

elif media < 7.5 and media >= 6:
    conceito = "C"

elif media < 6 and media >= 4:
    conceito = "D"

elif media < 4:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
        print("Aprovado!")

elif conceito == "D" or conceito == "E":
        print("Reprovado!")