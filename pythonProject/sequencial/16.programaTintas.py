#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
# usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input("Digite o tamanho da área desejada para ser pintada em metros: "))
#uma lata pinta 54m
litros = tamanho/3
latas = int(litros/18)


if litros % 18 != 0:
    latas += 1

valorTotal = latas * 80

print("A quantidade de latas que você irá precisar é de: ", latas, f" e o valor a ser pago é de: {valorTotal:.2f}")

