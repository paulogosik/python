numeros = []
numerosContrario = []
maiorElemento = 0
somaElementos = 0
i = 0

while i < 20:
    num = int(input(f"=> Informe um número inteiro: "))
    if num not in numeros:
        somaElementos += num
        if (i % 2 == 0) and (num > maiorElemento):
            maiorElemento = num
        numeros.append(num) 
    i += 1

i = len(numeros) - 1
while i >= 0:
    numerosContrario.append(numeros[i])    
    i -= 1

print("-----------------------------")
print(f"=> Lista: {numeros}")
print("-----------------------------")
print(f"=> Lista de trás para frente: {numerosContrario}")
print("-----------------------------")
print(f"=> Soma dos elementos da lista: {somaElementos}")
print("-----------------------------")
print(f"=> Maior elemento em posição par: {maiorElemento}")