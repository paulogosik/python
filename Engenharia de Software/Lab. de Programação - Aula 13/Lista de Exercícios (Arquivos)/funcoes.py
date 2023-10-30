def separar_arquivos():
    produtosEstoque = []
    produtosForaEstoque = []

    arquivo = open("produtos.txt", "r", encoding="utf8")
    produtos = arquivo.readlines()

    for pos, produto in enumerate(produtos):
        produto = produto.split(",")
        if pos != 0:
            if produto[1] == "Sim\n" or produto[1] == "Sim":
                produtosEstoque.append(produto[0])
            else:
                produtosForaEstoque.append(produto[0])

    return produtosEstoque, produtosForaEstoque


def arquivoEstoque(produtos):
    tamanhoLista = len(produtos) - 1
    arquivo_emestoque = open("emestoque.txt", "w", encoding="utf8")

    for posicao, produto in enumerate(produtos):
        if posicao != tamanhoLista:
            arquivo_emestoque.writelines(f"{produto}\n")
        else:
            arquivo_emestoque.writelines(produto)


def arquivoForaEstoque(produtos):
    tamanhoLista = len(produtos) - 1
    arquivo_emestoque = open("foradeestoque.txt", "w", encoding="utf8")

    for posicao, produto in enumerate(produtos):
        if posicao != tamanhoLista:
            arquivo_emestoque.writelines(f"{produto}\n")
        else:
            arquivo_emestoque.writelines(produto)
