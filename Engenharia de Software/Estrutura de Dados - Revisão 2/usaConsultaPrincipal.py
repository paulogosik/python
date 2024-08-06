import Tree 

t = Tree.Tree()

t.insere(4)
t.insere(2)
t.insere(1)
t.insere(3)
t.insere(6)
t.insere(5)
t.insere(9)
t.insere(8)
t.insere(7)
t.insere(10)
t.insere(10)
t.insere(11)

#questão 1
print("\n-------------------------\n")
print("Filhos de pais pares Esquerda -> Direita: ")
t.filhos_de_pai_par()
print("\n\n-------------------------\n")

#questão 2
print("Menor valor da árvore: ")
print(t.descendente_mais_a_esquerda())
print("\n-------------------------\n")

#questão 3
print("Menor filho da subarvore: ")
t.imprime_menor_filho(6)
print("\n-------------------------\n")

"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
from TREE import Tree

# Cria uma instância da árvore
minha_arvore = Tree()

# Insere valores na árvore
minha_arvore.insere(10)
minha_arvore.insere(5)
minha_arvore.insere(15)
minha_arvore.insere(3)
minha_arvore.insere(7)

# Busca valores na árvore
print(f"Busca pelo valor 7: {'Encontrado' if minha_arvore.busca(7) else 'Não encontrado'}")
print(f"Busca pelo valor 8: {'Encontrado' if minha_arvore.busca(8) else 'Não encontrado'}")

# Imprime a árvore em diferentes ordens
print("PreOrdem:", end=" ")
minha_arvore.preOrdem()
print("\nInOrdem:", end=" ")
minha_arvore.inOrdem()
print("\nPosOrdem:", end=" ")
minha_arvore.posOrdem()

# Altura da árvore
print(f"\nAltura da árvore: {minha_arvore.altura()}")

# Nível de um valor específico
print(f"Nível do valor 7: {minha_arvore.nivel(7)}")

# Imprime as folhas da árvore
print("Folhas da árvore:", end=" ")
minha_arvore.printFolhas()

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
from TREE import Tree

# Cria uma instância da árvore
minha_arvore = Tree()

# Insere valores na árvore
minha_arvore.insere(10)
minha_arvore.insere(5)
minha_arvore.insere(15)
minha_arvore.insere(3)
minha_arvore.insere(7)

# Busca valores na árvore
print(f"Busca pelo valor 7: {'Encontrado' if minha_arvore.busca(7) else 'Não encontrado'}")
print(f"Busca pelo valor 8: {'Encontrado' if minha_arvore.busca(8) else 'Não encontrado'}")

# Contar folhas
print(f"\nNúmero de folhas: {minha_arvore.contarFolhas()}")

# Imprimir nós internos
print("Nós internos:", end=" ")
minha_arvore.printNosInternos()

# Verificar se a árvore é completa
print(f"\nÁrvore é completa: {'Sim' if minha_arvore.verificarCompleta() else 'Não'}")

# Verificar se a árvore é perfeita
print(f"Árvore é perfeita: {'Sim' if minha_arvore.verificarPerfeita() else 'Não'}")

# Soma dos nós internos
print(f"Soma dos nós internos: {minha_arvore.somaNosInternos()}")

# Média dos valores dos nós
print(f"Média dos valores dos nós: {minha_arvore.mediaValores()}")

# Imprimir caminho da raiz até o nó com valor específico
print("Caminho da raiz até o nó com valor 7:", end=" ")
minha_arvore.printCaminhoRaizAteNo(7)

# Imprimir caminho do nó até a raiz
print("\nCaminho do nó com valor 7 até a raiz:", end=" ")
minha_arvore.printCaminhoNoAteRaiz(7)

# Verificar se a subárvore que contém um valor específico é completa
print(f"\nSubárvore com valor 5 é completa: {'Sim' if minha_arvore.verificarSubarvoreCompleta(5) else 'Não'}")

# Verificar se a subárvore que contém um valor específico é perfeita
print(f"Subárvore com valor 5 é perfeita: {'Sim' if minha_arvore.verificarSubarvorePerfeita(5) else 'Não'}")

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
from TREE import Tree

# Cria uma instância da árvore
minha_arvore = Tree()

# Insere valores na árvore
minha_arvore.insere(10)
minha_arvore.insere(5)
minha_arvore.insere(15)
minha_arvore.insere(3)
minha_arvore.insere(7)

# Busca valores na árvore
print(f"Busca pelo valor 7: {'Encontrado' se minha_arvore.busca(7) else 'Não encontrado'}")
print(f"Busca pelo valor 8: {'Encontrado' se minha_arvore.busca(8) else 'Não encontrado'}")



# Soma dos nós ímpares
print(f"\nSoma dos nós ímpares: {minha_arvore.soma_nos_impares()}")

'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
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

# Busca valores na árvore
print(f"Busca pelo valor 7: {'Encontrado' se minha_arvore.busca(7) else 'Não encontrado'}")
print(f"Busca pelo valor 8: {'Encontrado' se minha_arvore.busca(8) else 'Não encontrado'}")

# Contar e imprimir nós ímpares
print(f"Quantidade de nós ímpares: {minha_arvore.qtNumeroImpares()}")
print("Nós ímpares no nó com valor 5:", end=" ")
minha_arvore.numeroImparesNo(5)

# Soma dos nós ímpares
print(f"\nSoma dos nós ímpares: {minha_arvore.soma_nos_impares()}")

# Soma dos filhos de pais ímpares
print(f"Soma dos filhos de pais ímpares: {minha_arvore.soma_filhos_de_pais_impares()}")

# Contar o número total de nós
print(f"Número total de nós na árvore: {minha_arvore.contar_nos()}")

# Encontrar a subárvore com maior soma
maior_subarvore = minha_arvore.subarvore_maior_soma()
if maior_subarvore:
    print(f"Subárvore com maior soma: {maior_subarvore.info}")
else:
    print("Não há subárvores.")

# Listar nós com filho único
nos_filho_unico = minha_arvore.nos_com_filho_unico()
print("Nós com filho único:")
for no in nos_filho_unico:
    print(no)

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# Encontrar o tio de um nó específico
tio_valor = minha_arvore.get_tio(7)
if tio_valor is not None:
    print(f"Tio do nó com valor 7: {tio_valor}")
else:
    print("O nó com valor 7 não tem tio.")

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
