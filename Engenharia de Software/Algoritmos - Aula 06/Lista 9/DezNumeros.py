i = 0
quantP = 0
quantI = 0
nP = 0

while i < 10:
    i += 1
    n = int(input("=> Informe um número: "))
    print(f"=> Número: {n}\n"
          f"= > Antecessor: {n -1} | Sucessor: {n + 1}")
    print("-------------------------")

    if (n % 2 == 0) and n > 0 and n > 50:
        quantP += 1
    elif (n % 2 != 0):
        quantI += 1
    if n > 0:
        nP += 1

porcent = (nP * 100) / 10

print(f"=> Número pares, positivos e maiores que 50: {quantP}")
print(f"=> Números ímpares: {quantI}")
print(f"=> Porcentagem de números positivos: {porcent}%")