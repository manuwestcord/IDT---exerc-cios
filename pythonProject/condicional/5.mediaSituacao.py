nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media == 10:
    print("O aluno foi aprovado com Distinção")

elif media >= 7 and media != 10:
    print("O aluno foi aprovado!")

elif media < 7:
    print("O aluno foi reprovado!")

