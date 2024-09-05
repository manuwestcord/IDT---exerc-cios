#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
# são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
# programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo

valorHora = float(input("Digite o quanto você ganha por hora: R$ "))
horasTrabalhadas = float(input("Digite a quantidade de horas que você trabalha no mês: "))

salarioBruto = valorHora * horasTrabalhadas
valorINSS = 0.08 * salarioBruto
valorIR = 0.11 * salarioBruto
sindicato = 0.05 * salarioBruto
salarioLiquido = salarioBruto - (valorINSS + valorIR + sindicato)

print(f"O seu salário bruto é de: R$ {salarioBruto:.2f}")
print(f"O valor entregue para o INSS é de: R$ {valorINSS:.2f}")
print(f"O valor entregue para o sindicato é de: R$ {sindicato:.2f}")
print(f"O seu valor entregue para o imposto de renda é de: R$ {valorIR:.2f}")
print(f"O seu salário líquido é de: R$ {salarioLiquido:.2f}")
