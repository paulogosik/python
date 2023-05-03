numeros = []
i = 0
somaPares = 0

while i < 6:
    numeros.append(int(input(f"=> Informe um número {i+1}: ")))
    i += 1

i = 0
print("--------------------------")
print(f"=> Elementos da lista:")
while i < len(numeros):
    print(numeros[i])
    
    if numeros[i] % 2 == 0:
        somaPares += numeros[i]
    
    i += 1

i = 0
print("--------------------------")
print(f"=> Três primeiros elementos:")
while i < 3:
    print(numeros[i])
    i += 1

print("--------------------------")
print(f"=> Soma dos elementos pares: {somaPares}")