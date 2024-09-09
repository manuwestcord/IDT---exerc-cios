capacidadeTanque = float(input("Informe a capacidade total do tanque (em litros): "))
litrosAbastecidos = float(input("Informe a quantidade de litros abastecidos: "))
quilometragem_percorrida = float(input("Informe a quilometragem percorrida desde o último abastecimento: "))

# Calcula o consumo médio (km/l)
consumo_medio = quilometragem_percorrida / litros_abastecidos

# Calcula a autonomia antes do abastecimento
autonomia_restante = (capacidade_tanque - litros_abastecidos) * consumo_medio

# Exibe os resultados
print(f"O consumo médio foi de {consumo_medio:.2f} km/l.")
print(f"A autonomia que o carro ainda teria antes do abastecimento era de {autonomia_restante:.2f} km.")
