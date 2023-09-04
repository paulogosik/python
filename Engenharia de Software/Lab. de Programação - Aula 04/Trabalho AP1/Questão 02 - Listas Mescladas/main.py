import funcoes # type: ignore
lista1 = ["A", "B", "C", "D", "E"]
lista2 = [0, 1, 2, 3, 4]

print(f"=> Lista 1: {lista1}")
print(f"=> Lista 2: {lista2}")
listaFinal = funcoes.juntar_listas(lista1, lista2)
print(f"=> Lista final: {listaFinal}")