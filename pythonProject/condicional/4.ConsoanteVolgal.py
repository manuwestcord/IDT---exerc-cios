#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra para saber se é volgal ou consoante: ")).lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Essa letra é uma volgal")

else:
    print("Essa letra é uma consoante")