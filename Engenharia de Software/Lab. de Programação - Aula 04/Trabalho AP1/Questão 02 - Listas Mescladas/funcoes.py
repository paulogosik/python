def juntar_listas(lista1, lista2):
    listaFinal = []
    i = 0
    while i < len(lista1):
        listaFinal.append(lista1[i])
        listaFinal.append(lista2[i])
        
        i += 1
    
    return listaFinal