lista = []
contadorPares = 0
menorNumero = 0
somaDezElementos = 0

while len(lista) < 20:
    num = int(input(f"=> Informe um número inteiro {len(lista) + 1}: "))
    
    if num % 2 == 0:
        contadorPares += 1 
    if len(lista) < 10:
        somaDezElementos += num
    if menorNumero == 0:
        menorNumero = num
    elif menorNumero > num:
        menorNumero = num
    
    lista.append(num)

print(f"----------------------------")
print(f"=> Quantidade de número pares: {contadorPares}")
print(f"=> Menor elemento da lista: {menorNumero}")
print(f"=> Soma dos 10 primeiro números: {somaDezElementos}")