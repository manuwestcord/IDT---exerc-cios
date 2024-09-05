precoMorangoAte5kg = 2.50
precoMorangoAcima5kg = 2.20
precoMacaAte5kg = 1.80
precoMacaAcima5kg = 1.50

kgMorango = float(input("Digite a quantidade de morangos em Kg: "))
kgMaca = float(input("Digite a quantidade de maçãs em Kg: "))

if kgMorango <= 5:
    precoMorango = kgMorango * precoMorangoAte5kg
else:
    precoMorango = kgMorango * precoMorangoAcima5kg

if kgMaca <= 5:
    precoMaca = kgMaca * precoMacaAte5kg
else:
    precoMaca = kgMaca * precoMacaAcima5kg

valorTotal = precoMorango + precoMaca

if kgMorango + kgMaca > 8 or valorTotal > 25:
    valorTotal *= 0.90

print(f"Valor a ser pago: R$ {valorTotal:.2f}")
