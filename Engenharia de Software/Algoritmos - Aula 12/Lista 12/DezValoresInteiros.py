lista = []
listaModificada = []
i = 0

while i < 10:
    num = int(input(f"=> Informe um número {i+1}: "))
    lista.append(num)
    i += 1

primeiroNum = lista[0]
ultimoNum = lista[len(lista)-1]

i = 0
while i < len(lista):
    if i == 0:
        listaModificada.append(ultimoNum)
    elif i == (len(lista) - 1):
        listaModificada.append(primeiroNum)
    else:
        listaModificada.append(lista[i])
    i += 1

print("-----------------------")
print(f"=> Lista final: {listaModificada}")