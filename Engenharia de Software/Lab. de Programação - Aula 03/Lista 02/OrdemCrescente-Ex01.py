# Utilizando sort() para resolver ------------------------------------------
def ordena_tamanho(lista):
    lista_ordenada = lista[:]

    lista_ordenada.sort(key=len)

    return lista_ordenada


lista = ["Maria", "João", "Chico"]
novaLista = ordena_tamanho(lista)
print(f"=> Lista antes da funcao: {lista}")
print(f"=> Lista após a funcao: {novaLista}")

# "Criando" a função sort() ------------------------------------------
# def ordena_tamanho(lista):
#     lista_ordenada = lista[:]

#     for nome in range(len(lista_ordenada)):
#         for nomes in range(len(lista_ordenada)):
#             if len(lista_ordenada[nome]) < len(lista_ordenada[nomes]):
#                 menor = lista_ordenada[nomes]
#                 lista_ordenada[nomes] = lista_ordenada[nome]
#                 lista_ordenada[nome] = menor
                
#     return lista_ordenada


# lista = ["Tress", "Dois", "Um"]
# novaLista = ordena_tamanho(lista)
# print(f"=> Lista antes da funcao: {lista}")
# print(f"=> Lista após a funcao: {novaLista}")