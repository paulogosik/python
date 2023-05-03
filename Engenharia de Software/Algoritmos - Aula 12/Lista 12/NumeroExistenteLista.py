lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
i = 0
cont = 0
contadorNumero = 0

num = int(input("=> Informe um número: "))
print("----------------------------")

while i < len(lista):
    if lista[i] == num:
        contadorNumero += 1
    i += 1
    
if num in lista:
    print("= > O número existe na lista.")
    print(f"=> Este número aparece {contadorNumero} vezes")
else:
    print("= > O número não existe na lista.")