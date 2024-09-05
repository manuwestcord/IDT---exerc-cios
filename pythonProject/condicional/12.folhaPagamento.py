valorHora = float(input("Digite quanto você ganha por hora: R$ "))
totalHoras = float(input("Digite quantas horas vc trabalha no mês: "))
desconto = 0
salarioBruto = (valorHora * totalHoras)
fgts = salarioBruto * 0.11
inss = salarioBruto * 0.1

if salarioBruto <= 900:
    desconto = 0

elif salarioBruto > 900 and salarioBruto <= 1500:
    desconto = 0.05

elif salarioBruto > 1500 and salarioBruto <= 2500:
    desconto = 0.1

elif salarioBruto > 2500:
    desconto = 0.2

impostoRenda = (salarioBruto * desconto)
totalDescontos = (impostoRenda + inss)
salarioLiquido = (salarioBruto - totalDescontos)

print("Salário Bruto: ( ", valorHora, " * ", totalHoras, f" )     : R${salarioBruto:.2f}\n "
    "(-) IR ( ", impostoRenda, f")                       : R$ {impostoRenda:.2f}\n (-) INSS (", inss,
      f"%)                    : R$ {inss:.2f}\n FGTS (11%)                             : R$ {fgts:.2f}\n "
      f"Total de Descontos                     : R$ {totalDescontos:.2f}\n"
      f" Salário Liquído                        : R$ {salarioLiquido:.2f}")