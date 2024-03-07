import Lee

lista = Lee.Lee(5)

print("-" * 30)
print("Lista:")
# lista.show()
lista.show_vetor()

print("-" * 30)
lista.inserir_inicio("C")
# print("Lista após inserir início C: (esperado - C)")
lista.show()
lista.show_vetor()

print("-" * 30)
lista.inserir_inicio("D")
# print("Lista após inserir início D: (esperado - DC)")
lista.show()
lista.show_vetor()