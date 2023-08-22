def ordem_alfabetica(palavras):
    novaLista = palavras
    novaLista.sort()
    
    return novaLista
    
lista = ["Maçã", "Pera", "Banana"]
print(f"=> Lista antes da ordenação: {lista}")
novaLista = ordem_alfabetica(lista)
print(f"=> Lista depois da ordenação: {novaLista}")