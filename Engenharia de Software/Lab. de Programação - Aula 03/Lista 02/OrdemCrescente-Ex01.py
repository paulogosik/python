# def ordena_tamanho(lista):
#     lista_ordenada = lista[:]
#
#     lista_ordenada.sort(key=len)
#
#     return lista_ordenada
#
#
# lista = ["Maria", "João", "Chico"]
# novaLista = ordena_tamanho(lista)
# print(f"=> Lista antes da funcao: {lista}")
# print(f"=> Lista após a funcao: {novaLista}")

# ------------------------------------------
def ordena_tamanho(lista):
    lista_ordenada = lista[:]

    for nome in lista_ordenada:
        for nomes in lista_ordenada:
            print(f"{nomes}")


lista = ["Maria", "João", "Chico"]
novaLista = ordena_tamanho(lista)
# print(f"=> Lista antes da funcao: {lista}")
# print(f"=> Lista após a funcao: {novaLista}")