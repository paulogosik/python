i = 1

x = int(input("=> Digite um número inteiro: "))
print("-------------------------------")

while x / 2 > 1:
    x = x / 2
    i += 1

print(f"=> Última divisão: {x:.2f} divido por 2 igual a: {(x / 2):.2f}")
print(f"=> Número de divisões feitas: {i}")