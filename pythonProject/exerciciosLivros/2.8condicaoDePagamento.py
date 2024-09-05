preco = float(input("Digite o preço do produto: "))
condicaoPagamento = int(input("Selecione o modo de pagamento\n 1- À vista em dinheiro ou cheque, 10% de desconto.\n "
                              "2- À vista no cartão de crédito, 5% de desconto.\n 3- Em duas vezes, o preço normal de etiqueta sem juros.\n "
                              "4- Em três vezes, preço normal de etiqueta com 10% de juros: "))
if condicaoPagamento == 1:
    desconto = preco * 0.1
    preco = (preco - desconto)
    print(f"O preço ficará no valor de: R${preco:.2f} e no dinheiro ou cheque à vista.")

elif condicaoPagamento == 2:
    desconto = preco * 0.05
    preco = (preco - desconto)
    print(f"O preço ficará no valor de: R${preco:.2f} no cartão de crédio à vista.")

elif condicaoPagamento == 3:
    print(f"O preço ficará no valor de: R${preco:.2f} no cartão de crédio parcelado em 2x.")

elif condicaoPagamento == 4:
    desconto = preco * 0.1
    preco = (preco + desconto)
    print(f"O preço ficará no valor de: R${preco:.2f} no cartão de crédio parcelado em 3x.")

