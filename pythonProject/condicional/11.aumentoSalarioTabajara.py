salario = float(input("Digite o valor do seu salário: "))
aumento = 0


if salario <= 280:
    aumento = 0.2

if salario >= 281 and salario <= 700:
    aumento = 0.15

if salario >= 701 and salario <= 1500:
    aumento = 0.1

if salario >= 1501:
    aumento = 0.05

totalAumento= (salario * aumento)
totalSalario = (salario + totalAumento)

print(f"O seu salário anterior era de R$ {salario:.2f}, o seu percentual aplicado é de ", aumento * 100,
      f"%, o valor do aumento foi de R$ {totalAumento:.2f} e o seu salário após o aumento é de R$ {totalSalario:.2f}")