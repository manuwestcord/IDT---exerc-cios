numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O número 1 é o maior destes")

elif numero2 > numero1 and numero2 > numero3:
    print("O número 2 é o maior destes")

elif numero3 > numero2 and numero3 > numero2:
    print("O número 3 é o maior destes")

else:
    print("O maior número é igual em duas ou mais ocasiões: ")

