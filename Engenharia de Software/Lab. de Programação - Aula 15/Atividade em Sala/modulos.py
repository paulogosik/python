import json

def carregarDados(localizacao):
    arquivo = open(localizacao, "r", encoding="utf8")
    texto = arquivo.read()
    if len(texto) == 0:
        return dict()
    dicionario = json.loads(texto)
    arquivo.close()
    return dicionario


def gravarDados(localizacao, dicionario):
    database = carregarDados(localizacao)
    for key, value in dicionario.items():
        database[key] = value

    arquivo = open(localizacao, "w", encoding="utf8")
    texto = json.dumps(database, indent=4)
    arquivo.write(texto)
    arquivo.close()


def verificarChave(localizacao, chave):
    dicionario = carregarDados(localizacao)

    if dicionario.get(chave):
        return True
    else:
        return False


def alterarDados(localizacao, chave):
    print("-" * 15)
    database = carregarDados(localizacao)

    print("Qual dado você deseja alterar?")
    for k, dicionario in database.items():
        if k == chave:
            for pos, dado in enumerate(dicionario.keys()):
                print(f"\t[{pos + 1}] {dado}")
    print("\t[0] Todos")
    opc = int(input(">>> "))

    if opc == 0:
        for k, dicionario in database.items():
            if k == chave:
                for c in dicionario.keys():
                    dicionario[c] = input(f"{c}: ")
    else:
        for k, dicionario in database.items():
            if k == chave:
                for pos, dado in enumerate(dicionario.keys()):
                    if pos + 1 == opc:
                        if dado == "Quantidade":
                            dicionario[dado] = int(input(f"{dado}: "))
                        else:
                            dicionario[dado] = input(f"{dado}: ")

    arquivo = open(localizacao, "w", encoding="utf8")
    texto = json.dumps(database, indent=4)
    arquivo.write(texto)
    arquivo.close()


def excluirItem(localizacao, chave):
    database = carregarDados(localizacao)
    del database[chave]

    arquivo = open(localizacao, "w", encoding="utf8")
    texto = json.dumps(database, indent=4)
    arquivo.write(texto)
    arquivo.close()

    print("Item excluído com sucesso!")


def pesquisarLivro(localizacao, titulo):
    livrosComTitulos = []
    tamanhoTitulo = len(titulo)
    database = carregarDados(localizacao)
    for isbn, livros in database.items():
        for key, value in livros.items():
            if key == "Titulo":
                if value[0:tamanhoTitulo] == titulo:
                    livrosComTitulos.append(isbn)

    if len(livrosComTitulos) == 0:
        print("Não foi encontrado nenhum livro com este título.")
    else:
        print("")
        for isbn, livros in database.items():
            if isbn in livrosComTitulos:
                print(f"ISBN: {isbn}")
                for key, value in livros.items():
                    print(f"{key}: {value}")
                print("")


def realizarVenda(localizacaoClientes, localizacaoLivros, dicionario):
    isbn = quantidadeCliente = None
    for cliente in dicionario.values():
        isbn = cliente.pop("ISBN")
        quantidadeCliente = cliente.get("Quantidade comprada")

    databaseLivros = carregarDados(localizacaoLivros)
    for chaveLivro, livro in databaseLivros.items():
        if chaveLivro == isbn:
            quantidadeLivro = livro.get("Quantidade")
            if quantidadeLivro > quantidadeCliente:
                livro["Quantidade"] = quantidadeLivro - quantidadeCliente
            else:
                return "Quantidade requisitada maior que a quantidade disponível."

    arquivo = open(localizacaoLivros, "w", encoding="utf8")
    texto = json.dumps(databaseLivros, indent=4)
    arquivo.write(texto)
    arquivo.close()

    gravarDados(localizacaoClientes, dicionario)
    return "Venda realizada com sucesso!"


def relatoriaVendas(localizacao):
    database = carregarDados(localizacao)
    for key, value in database.items():
        print(f"CPF: {key}")
        for chave, valor in value.items():
            print(f"{chave}: {valor}")
        print("-" * 15)
