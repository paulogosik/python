i = 0
lucroTotal = 0
quantTotal = 0

while i < 5:
    estoque = int(input("=> Qual a quantidade de produtos em estoque? "))
    precoC = float(input("=> Qual o preço de custo? "))
    precoV = float(input("=> Qual o preço de venda? "))
    
    lucro = precoV - precoC
    lucroTotal = lucroTotal + (lucro * estoque)

    print(f"=> Lucro individual: R${lucro}")
    print("-----------------------------")

    i += 1

print(f"=> Valor arrecadado se todos os produtos expostos forem vendidos: R${lucroTotal}\n")