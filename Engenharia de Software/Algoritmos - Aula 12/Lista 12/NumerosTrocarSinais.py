numeros = []

num = int(input(f"=> Informe um número inteiro: "))

while num != 0:
    num = num * -1
    numeros.append(num)
    num = int(input(f"=> Informe um número inteiro: "))

print(f"--------------------------")
print(f"=> Lista criada (com sinais trocados): {numeros}")