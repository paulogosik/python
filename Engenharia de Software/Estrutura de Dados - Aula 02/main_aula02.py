import Les

lista = Les.Les(5)
# print(lista)
# print(lista.vetor)
lista.inserir_fim('A')
lista.inserir_fim('B')
lista.inserir_fim('C')
lista.inserir_fim('D')
# lista.remover_fim()
# # lista.remover_fim()
# lista.inserir_fim('C')
# if not lista.esta_vazia():
#     lista.remover_fim()
lista.show()
lista.inserir_apos('S', 'B')
lista.show()