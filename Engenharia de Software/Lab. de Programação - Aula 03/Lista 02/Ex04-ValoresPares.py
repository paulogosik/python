def lista_valores_pares(lista):
    listaPares = []
    for valor in range(len(lista)):
        if valor % 2 == 0:
            listaPares.append(lista[valor])
    
    return listaPares

lista = [1, 2, 3, 4, 5, 6]
print(f"=> Lista: {lista}")
print(f"=> Lista com posições pares: {lista_valores_pares(lista)}")