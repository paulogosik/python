nomes = []
idades = []
nomesAcimaMedia = []
totalIdades = 0

while len(nomes) < 5:
    nome = input(f"=> Informe um nome ({len(nomes) + 1}): ")
    idade = int(input(f"=> Informe uma idade ({len(idades) + 1}): "))
    print("--------------------------")
    
    totalIdades += idade
    
    nomes.append(nome)
    idades.append(idade)

i = 0
while i < len(nomes):
    print(f"=> {i} {nomes[i]} {idades[i]}")
    
    i += 1

print("--------------------------")
mediaIdades = totalIdades / len(idades)
print(f"=> Média das idades: {mediaIdades}")
print("--------------------------")

i = 0
while i < len(idades):
    if idades[i] > mediaIdades:
        nomesAcimaMedia.append(nomes[i])
    i += 1

print(f"=> Pessoas com idade acima da média: {nomesAcimaMedia}")