def separar_pares_impares(listaGeral):
    listaPar = []
    listaImpar = []
    
    for valor in listaGeral:
        if valor % 2 == 0:
            listaPar.append(valor)
        else:
            listaImpar.append(valor)
            
    print(f"=> Valores pares: {listaPar}")
    print(f"=> Valores ímpares: {listaImpar}")
    
listaGeral = []
i = 0
while i < 10:
    num = float(input(f"=> Informe um número qualquer {i + 1}: "))
    listaGeral.append(num)
    i += 1
    
separar_pares_impares(listaGeral)