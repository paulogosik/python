# DECLARAÇÃO DE VARIÁVEIS
i = 0
compraTotal = 0
valorExatoTotal = 0
trocoTotal = 0

while i < 80:
    i += 1

    # INPUT DE VALORES
    print("----------------------------")
    compra = float(input("=> Informe o valor da compra: "))
    dinheiro = float(input("=> Informe o valor em dinheiro entregue pelo cliente: "))

    # ARMAZENANDO DADOS PARA A MÉDIA DOS VALORES DE COMPRA
    compraTotal = compraTotal + compra

    # CONDIÇÕES DE VALORES ENTRE O DINHEIRO ENTREGUE E O VALOR DA COMPRA
    if dinheiro < compra:
        valor = compra - dinheiro
        print(f"=> Valor insuficente! Falta R${valor:.2f}")
    elif dinheiro == compra:
        valorExatoTotal = valorExatoTotal + 1
        print("=> Valor exato! Não tem troco.")
    else: 
        troco = dinheiro - compra
        trocoTotal = trocoTotal + troco
        print(f"=> Valor superior! Troco de R${troco:.2f}")

# CALCULOS DE VALORES FORA DO WHILE, ALGO TOTAL
mediaDeCompra = compraTotal / 80

# FORA DO WHILE, PRINTS A SEREM EXECUTADOS APENAS UMA VEZ (AO FINAL)
print("----------------------------")
print(f"=> Quantidade de pessoas que entregaram o valor exato: {valorExatoTotal}")
print(f"=> Valor total de troco entregue: R${trocoTotal:.2f}")
print(f"=> Média dos valores de compra: R${mediaDeCompra:.2f}")