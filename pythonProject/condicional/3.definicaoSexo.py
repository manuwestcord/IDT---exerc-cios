#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
# escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Digite M se for do sexo masculino ou F se for do sexo feminino: "))

if sexo == "M" or sexo =="m":
    print("M - masculino")

elif sexo == "F" or sexo == "f":
    print ("F - feminino")

else:
    print("Sexo inválido")