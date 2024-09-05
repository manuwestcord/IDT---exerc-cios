CPF = input("Digite o CPF: ")
dependentes = int(input("Digite o número de dependentes: "))
rendaMensal = float(input("Digite o valor da sua renda mensal: "))
salarioMinimo = float(input("Digite o salário mínimo: "))
calculoImposto = 0

descontoDependente = dependentes * 5

rendaLiquida = rendaMensal * (1 - (descontoDependente / 100))

proporcaoSalario = rendaLiquida / salarioMinimo

if proporcaoSalario <= 2:
    calculoImposto = 0

elif proporcaoSalario > 2 and proporcaoSalario <= 3:
    calculoImposto = 5

elif proporcaoSalario > 3 and proporcaoSalario <= 5:
    calculoImposto = 10

elif proporcaoSalario > 5 and proporcaoSalario <= 7:
    calculoImposto = 15

else:
    calculoImposto = 20

valorPagarImposto = rendaLiquida * (calculoImposto / 100)

valorReceber = rendaLiquida - valorPagarImposto

print(f"O valor a se pagar de imposto é de  R$ {valorPagarImposto:.2f}")

print(f"O valor a receber é de R$ {valorReceber:.2f}")