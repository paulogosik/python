lista = [10, 5, 8, 20, 50, 10, 5, 8, 8, 60, 10, 5, 5, 3, 50]
posicoesPares = []
maiorElemento = 0
somaPositivos = 0

i = 0
print("--------------------------")
while i < len(lista):
    
    if maiorElemento < lista[i]:
        maiorElemento = lista[i]
    if lista[i] > 0:
        somaPositivos += lista[i]
    if lista[i] % 2 == 0:
        posicoesPares.append(i)
    
    i += 1
print(f"=> Maior elemento: {maiorElemento}")
print("--------------------------")
print(f"=> Soma dos elementos positivos: {somaPositivos}")

i = 0
print("--------------------------")
print(f"=> Cinco primeiros elementos:")
while i < 5:
    print(lista[i])
    i += 1
    
print("--------------------------")
print(f"=> Posições dos números pares: {posicoesPares}")