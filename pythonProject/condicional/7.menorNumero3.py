numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    print("O primeiro número é o menor destes")

elif numero2 < numero1 and numero2 < numero3:
    print("O segundo número é o menor destes")

elif numero3 < numero2 and numero3 < numero2:
    print("O terceiro número é o menor destes")

else:
    print("O menor número é igual em duas ou mais ocasiões: ")