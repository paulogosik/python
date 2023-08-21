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

    for i in len(lista_ordenada):
        print(lista_ordenada[i])


lista = ["Maria", "João", "Chico"]
novaLista = ordena_tamanho(lista)
# print(f"=> Lista antes da funcao: {lista}")
# print(f"=> Lista após a funcao: {novaLista}")