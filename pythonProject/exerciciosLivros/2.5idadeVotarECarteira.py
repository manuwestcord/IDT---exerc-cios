#Faça um algoritimo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também, verifique e mostre
# se ela já tem idade para votar (16 anos ou mais) e para conseguir a Carteira de Habilitação (18 anos ou mais).
anoNascimento = int(input("Digite o seu ano de nascimento: "))

idade2024 = (2024 - anoNascimento)
print("Sua idade é de ", idade2024, " anos")

if idade2024 >= 16:
    print("Você já pode votar!")

if idade2024 >= 18:
    print("Você já pode tirar a Carteira de Habilitação!")
