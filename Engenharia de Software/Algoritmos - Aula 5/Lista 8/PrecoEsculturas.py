i = 0
lucroTotal = 0
precoEspecif = 0

while i < 5:
    i += 1

    precoC = float(input(f"=> Qual o valor de compra da escultura {i}? "))
    precoV = float(input(f"=> Qual o valor de venda da escultura {i}? "))
    lucro = precoV - precoC
    lucroTotal = lucroTotal + lucro
    print(f"=> O lucro da escuultura {i} foi de: R${lucro}")
    print('-----------------------------')

    if precoC >= 20 and precoC <= 50:
        precoEspecif += 1
    
print(f"=> Número de esculturas entre R$20 e R$50: {precoEspecif}")
print(f"=> Lucro total: R${lucroTotal}")
    
