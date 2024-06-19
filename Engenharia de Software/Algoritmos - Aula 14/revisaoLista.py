# Criação de lista: ---------------------------
minha_lista = [1, 2, 3, 4, 5]
lista_vazia = []

# Descobrir tamanho da lista: ---------------------------
    # Quando temos que descobrir o tamanho de uma lista, usamos o len(). Exemplo: lista_exemplo.len()
listaAlunos = ["Ana", "Beto", "Paulo"]
print(listaAlunos.len()) # O resultado dessa linha é 3, pois há 3 elementos na lista.
if listaAlunos.len() > 4:
    print("Maior que quatro.") # Só vai printar se a lista for maior que 4.


# Existência de elementos: ---------------------------
    # Nós usamos 'in' para verificar se há o elemento na lista.
if "Ana" in listaAlunos:
    print("Existe na lista!")
else:
    print("Não existe na lista!")
    

# Inserindo elementos na lista: ---------------------------
    # Quando inserimos elementos numa lista, usamos o append(). Exemplo: lista_exemplo.append('elemento')
listaAlunos = ["Ana", "Beto", "Paulo"]
listaAlunos.append("Maria") # Inserimos na listaAlunos o elemento 'Maria', usando o append()