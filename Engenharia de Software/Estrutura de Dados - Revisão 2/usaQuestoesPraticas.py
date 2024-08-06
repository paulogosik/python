from TREE import Tree

# Cria uma instância da árvore
minha_arvore = Tree()

# Insere valores na árvore
minha_arvore.insere(10)
minha_arvore.insere(5)
minha_arvore.insere(15)
minha_arvore.insere(3)
minha_arvore.insere(7)
minha_arvore.insere(12)
minha_arvore.insere(18)

# Exemplo de uso da função num_nos_com_filho
print(f"Número de nós com pelo menos um filho: {minha_arvore.num_nos_com_filho()}")

# Exemplo de uso da função contaDescendentes
valor = 5
print(f"Quantidade de descendentes do valor {valor}: {minha_arvore.contaDescendentes(valor)}")

# Exemplo de uso da função printCaminho
valor = 7
print(f"Caminho da raiz até o nó com valor {valor}: ", end="")
minha_arvore.printCaminho(valor)
print()

# Exemplo de uso da função somaFolhasDescendentes
valor = 5
print(f"Soma dos nós-folha descendentes do valor {valor}: {minha_arvore.somaFolhasDescendentes(valor)}")

# Exemplo de uso da função maioresQue
x = 10
print(f"Valores na árvore maiores que {x}: ", end="")
minha_arvore.maioresQue(x)
print()

# Exemplo de uso da função paiDe
x = 7
print(f"Pai do nó com valor {x}: ", end="")
minha_arvore.paiDe(x)
print()

# Exemplo de uso da função imprimePares
print("Valores pares em ordem decrescente: ", end="")
minha_arvore.imprimePares()
print()

# Exemplo de uso da função soma_elementos
print(f"Soma de todos os elementos da árvore: {minha_arvore.soma_elementos()}")

# Exemplo de uso da função nivel_valor
valor = 7
print(f"Nível do valor {valor}: {minha_arvore.nivel_valor(valor)}")

# Exemplo de uso da função menor_elemento
print(f"Menor elemento da árvore: {minha_arvore.menor_elemento()}")

# Exemplo de uso da função maior_elemento
print(f"Maior elemento da árvore: {minha_arvore.maior_elemento()}")

# Exemplo de uso da função imprime_decrescente
print("Elementos da árvore em ordem decrescente: ", end="")
minha_arvore.imprime_decrescente()
print()
