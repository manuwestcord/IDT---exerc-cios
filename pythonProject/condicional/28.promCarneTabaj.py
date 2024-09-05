precoFileDuploAte5kg = 4.90
precoFileDuploAcima5kg = 5.80
precoAlcatraAte5kg = 5.90
precoAlcatraAcima5kg = 6.80
precoPicanhaAte5kg = 6.90
precoPicanhaAcima5kg = 7.80

tipoCarne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ")
quantidadeKg = float(input("Digite a quantidade de carne em Kg: "))
tipoPagamento = input("Digite o tipo de pagamento (Dinheiro ou Cartão Tabajara): ")

precoKg = 0

if tipoCarne == "File Duplo":
    if quantidadeKg <= 5:
        precoKg = precoFileDuploAte5kg
    else:
        precoKg = precoFileDuploAcima5kg
elif tipoCarne == "Alcatra":
    if quantidadeKg <= 5:
        precoKg = precoAlcatraAte5kg
    else:
        precoKg = precoAlcatraAcima5kg
elif tipoCarne == "Picanha":
    if quantidadeKg <= 5:
        precoKg = precoPicanhaAte5kg
    else:
        precoKg = precoPicanhaAcima5kg
else:
    print("Tipo de carne inválido.")
    precoKg = 0

valorTotal = quantidadeKg * precoKg

if tipoPagamento == "Cartão Tabajara":
    desconto = valorTotal * 0.05
else:
    desconto = 0

valorFinal = valorTotal - desconto

print("\nCupom Fiscal:")
print(f"Tipo de Carne: {tipoCarne}")
print(f"Quantidade: {quantidadeKg:.2f} Kg")
print(f"Preço Total: R$ {valorTotal:.2f}")
print(f"Tipo de Pagamento: {tipoPagamento}")
print(f"Valor do Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valorFinal:.2f}")
