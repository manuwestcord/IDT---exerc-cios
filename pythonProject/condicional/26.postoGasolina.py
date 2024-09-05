precoAlcool = 1.90
precoGasolina = 2.50

tipoCombustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")
litros = float(input("Digite o número de litros vendidos: "))

precoLitro = 0
desconto = 0

if tipoCombustivel == 'A':
    precoLitro = precoAlcool
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipoCombustivel == 'G':
    precoLitro = precoGasolina
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo de combustível inválido.")
    precoLitro = 0

if precoLitro > 0:
    valorTotal = litros * precoLitro
    valorDesconto = valorTotal * desconto
    valorFinal = valorTotal - valorDesconto

    print(f"Valor a ser pago: R$ {valorFinal:.2f}")
