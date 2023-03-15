i = 0

cont = int(input("=> Qual a quantidade de repetições? "))

while i < cont:
    quant = int(input("=> Qual a quantidade de produtos? "))
    preco = float(input("=> Qual o preço do produto? "))
    valor = quant * preco
    print(f"=> Valor total gasto: R${valor:.2f}")
    i += 1