# Imprimir filhos de pais ímpares
print("Filhos de pais ímpares:", end=" ")
minha_arvore.filhos_de_pai_impar()

# Descendente mais à direita (maior valor da árvore)
maior_valor = minha_arvore.descendente_mais_a_direita()
print(f"\nMaior valor da árvore: {maior_valor}")

# Imprimir maior valor entre os descendentes do nó com valor 5
print("Maior valor entre os descendentes do nó com valor 5:", end=" ")
minha_arvore.imprime_maior_filho(5)
