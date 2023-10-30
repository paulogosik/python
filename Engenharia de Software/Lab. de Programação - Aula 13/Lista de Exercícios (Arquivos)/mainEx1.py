from funcoes import *

produtosEstoque, produtosForaEstoque = separar_arquivos()
print("Arquivos separados com sucesso!")

arquivoEstoque(produtosEstoque)
arquivoForaEstoque(produtosForaEstoque)
print("Arquivos de estoque criados com sucesso!")
