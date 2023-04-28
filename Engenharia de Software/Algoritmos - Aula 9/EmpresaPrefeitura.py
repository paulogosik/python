metragem = 1
maiorValorB = 0
valorTotal = 0

print("-----------------------------")
valorMinimo = float(input("=> Informe o valor mínimo: "))
metragem = float(input("=> Informe a metragem da casa (m²): "))

while metragem != 0:
    classe = input("=> Informe a classe da casa (A ou B): ")
    classe = classe.upper()
    
    if classe == "A":
        valor = metragem * 500
        print(f"=> Valor a ser pago de idenização ao proprietário: R${valor}")
    elif classe == "B":
        valor = metragem * 300
        if valor > maiorValorB:
            maiorValorB += valor
        print(f"=> Valor a ser pago de idenização ao proprietário: R${valor}")
    else:
        valor = metragem * valorMinimo
        print(f"=> Valor a ser pago de idenização ao proprietário: R${valor}")
    
    valorTotal += valor
        
    print("-----------------------------")
    metragem = float(input("=> Informe a metragem da casa (m²): "))

print("-----------------------------")
print(f"=> Valor total gasto pela prefeitura com idenização: R${valorTotal}")
print(f"=> Maior valor pago para idenizar uma casa da classe 'B': R${maiorValorB}")  