listaVasos = [['V01', 100.00, 50.00],
['V02', 80.00, 25.00],
['V03', 110.00, 60.00],
['V04', 230.00, 100.00],
['V05', 25.00, 30.00]]
listaVasosBaratos = []
i = 0
precoDeCustoTotal = 0

while i < len(listaVasos):
    precoDeCusto = listaVasos[i][1] + listaVasos[i][2]
    precoDeCustoTotal += precoDeCusto
    listaVasos[i].append(precoDeCusto)
    
    print(f"=> #{listaVasos[i][0]} - Preço de custo: R${listaVasos[i][3]}")
    i += 1
print("----------------------------")

print(f"=> Média do preço de custo: R${precoDeCustoTotal / len(listaVasos)}")
print("----------------------------")

i = 0
while i < len(listaVasos):
    if listaVasos[i][3] < (precoDeCustoTotal / len(listaVasos)):
        listaVasosBaratos.append(listaVasos[i][0])
    i += 1

print(f"=> Vasos com preço de custo mais barato que a média: {listaVasosBaratos}")
print("----------------------------")