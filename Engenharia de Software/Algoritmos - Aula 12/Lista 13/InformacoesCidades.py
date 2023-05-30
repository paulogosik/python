nomes = []
habitantes = []
superficies = []
i = 0

while i < 10:
    nome = input(f"=> {i + 1} - Informe o nome da cidade: ")
    populacao = int(input(f"=> {i + 1} - Informe a quantidade de habitantes da cidade: "))
    superficie = float(input(f"=> {i + 1} - Informe a superfície da cidade (em metros quadrados): "))
    
    nomes.append(nome)
    habitantes.append(populacao)
    superficies.append(superficie)
    
    print("--------------------------")
    
    i += 1
    
print(nomes)
print(habitantes)
print(superficies)

i = 0
while i < len(nomes):
    print("--------------------------")
    densidade = habitantes[i]/superficies[i]
    print(f"=> {nomes[i]} - {densidade} pessoas/m²")
    
    i += 1