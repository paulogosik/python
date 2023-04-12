i = 1
casasCanal4 = 0
pessoasCanal5 = 0

canal = int(input(f"=> Informe o canal da casa {i}: "))

while canal != 0:
    pessoas = int(input(f"=> Informe a quantidade de pessoa na casa {i}: "))
    i += 1
    
    if canal == 4:
        casasCanal4 += 1
    elif canal == 5:
        pessoasCanal5 += pessoas
          
    print("-------------------------------")
    canal = int(input(f"=> Informe o canal da casa {i}: "))
    
print("-------------------------------")
print(f"=> Quantide de casas em que se assistia o canal 4: {casasCanal4}")
print(f"=> Quantidade de pessoas que assistiam o canal 5: {pessoasCanal5}")    