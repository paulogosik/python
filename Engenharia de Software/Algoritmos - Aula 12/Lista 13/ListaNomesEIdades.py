nomes = []
idades = []
totalIdades = 0

while len(nomes) < 5:
    nome = input(f"=> Informe um nome ({len(nomes) + 1}): ")
    idade = int(input(f"=> Informe uma idade ({len(idades) + 1}): "))
    
    totalIdades += idade
    
    nomes.append(nome)
    idades.append(idade)