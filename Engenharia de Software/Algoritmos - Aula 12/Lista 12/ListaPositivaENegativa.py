lista = [-5,10,-8,-3,5,10,11,8,-9,10]
positivos = []
negativos = []
i = 0

while i < len(lista):
    if lista[i] >= 0:
        positivos.append(lista[i])
    elif lista[i] < 0:
        negativos.append(lista[i])
    i += 1

print(f"=> Positivos: ")
print(positivos)
print(f"=> Negativos: ")
print(negativos)