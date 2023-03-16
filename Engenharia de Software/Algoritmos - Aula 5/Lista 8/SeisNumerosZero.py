i = 0
zeros = 0
positivos = 0

while i < 6:
    i += 1
    num = int(input("=> Digite um número inteiro: "))
    if num > 0:
        print("=> O número digitado é positivo.")
        print('-------------------------')
        positivos += num
    elif num < 0:
        print("=> O número digitado é negativo.")
        print('-------------------------')
    else:
        print("=> O número digitado é igual a zero.")
        print('-------------------------')
        zeros += 1

print(f"=> Quantidade de zeros digitados: {zeros}")
print(f"=> Soma dos números positivos: {positivos}")