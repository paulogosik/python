def juntar_listas(lista1, lista2):
    listaGeral = []
    i = 0
    
    if len(lista1) > len(lista2):
        while i < len(lista2):
            listaGeral.append(lista1[i])
            listaGeral.append(lista2[i])
            i += 1
        while i < len(lista1):
            listaGeral.append(lista1[i])
            i += 1
    elif len(lista1) < len(lista2):
        while i < len(lista1):
            listaGeral.append(lista1[i])
            listaGeral.append(lista2[i])
            i += 1    
        while i < len(lista2):
            listaGeral.append(lista2[i])
            i += 1
    else:
        while i < len(lista1):
            listaGeral.append(lista1[i])
            listaGeral.append(lista2[i])
            i += 1
        
    return listaGeral
    
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3, 4, 5, 6]

print(f"=> Lista 1: {lista1}")
print(f"=> Lista 2: {lista2}")
listaGeral = juntar_listas(lista1, lista2)
print(f"=> Lista final: {listaGeral}")