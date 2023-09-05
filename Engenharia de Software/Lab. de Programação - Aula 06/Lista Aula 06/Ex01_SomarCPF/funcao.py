def somar_cpf(cpf):
    somaTotal = 0
    
    lista = cpf.split(".")
    parteFinal = lista[2].split("-")
    del lista[2]
    
    for item in parteFinal:
        lista.append(item)
    
    for item in lista:
        somaTotal += int(item)
    
    print(lista)
    
    return somaTotal