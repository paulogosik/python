import json

def carregarDados(localizacao):
    arquivo = open(localizacao, "r", encoding="utf8")
    texto = arquivo.read()
    dicionario = json.loads(texto)
    arquivo.close()
    return dicionario


def gravarDados(localizacao, dicionario):
    database = carregarDados(localizacao)
    if len(database) != 0:
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
    print(localizacao, titulo)
