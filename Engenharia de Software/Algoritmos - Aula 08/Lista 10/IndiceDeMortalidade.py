criancasMortas = 0
criancasPrematuras = 0
criancasEspecifico = 0
i = 1

criancasNascidas = input("=> Qual o número de crianças nascidas nesse período? ")
print("-------------------------------")
sexo = input(f"=> Qual o sexo da criança morta {i}? 'M' para masculino ou 'F' para feminino. ")
sexo = sexo.upper()

while sexo == "M" or sexo == "F":
    i += 1
    criancasMortas += 1 
    idade = int(input(f"=> Qual a idade da criança morta {i}? "))
    print("-------------------------------")
    
    if idade < 12:
        criancasPrematuras += 1
    elif idade >= 12 and sexo == "M":
        criancasEspecifico += 1
    
    sexo = input(f"=> Qual o sexo da criança morta {i}? 'M' para masculino ou 'F' para feminino. ")
    sexo = sexo.upper()

porcentagem = (criancasMortas * 100) / criancasNascidas
print("-------------------------------")
print(f"=> Porcentagem de crianças mortas em relação à crianças nascidas: {porcentagem:.2f}")
print(f"=> Quantidade de crianças que não chegaram a um ano de vida: {criancasPrematuras}")
print(f"=> Quantidade de crianças do sexo masculino que viveu um ano ou mais: {criancasEspecifico}")   