numero = int(input("Digite um valor qualquer de 3 digitos (ex: 123): "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10

numeroInvertido = (unidade * 100) + (dezena * 10) + centena
print(f"O número invertido é: {numeroInvertido}")