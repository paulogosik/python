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


def atualizarDados(localizacaoAlunos, localizacaoDisciplinas, codigo, disciplina):
    nomeDiscplina = nomeDoObjeto(localizacaoDisciplinas, disciplina)
    nomeAluno = nomeDoObjeto(localizacaoAlunos, codigo)
    databaseAlunos = carregarDados(localizacaoAlunos)
    databaseDisciplinas = carregarDados(localizacaoDisciplinas)
    
    # Atualizando o Aluno
    disciplinasExistentes = databaseAlunos[codigo].get("Disciplina(s)", False)
    if disciplinasExistentes:
        if nomeDiscplina in disciplinasExistentes.split(', '):
            return "Aluno já está cadastrado nesta disciplina."
        else:
            nomeDiscplina = f"{disciplinasExistentes}, {nomeDiscplina}"

    databaseAlunos[codigo]["Disciplina(s)"] = nomeDiscplina

    arquivo = open(localizacaoAlunos, "w", encoding="utf8")
    texto = json.dumps(databaseAlunos, indent=4)
    arquivo.write(texto)
    arquivo.close()
    
    # Atualizando a Disciplina
    alunosExistentes = databaseDisciplinas[disciplina].get("Aluno(s)", False)
    if alunosExistentes:
        nomeAluno = f"{alunosExistentes}, {nomeAluno}"

    databaseDisciplinas[disciplina]["Aluno(s)"] = nomeAluno

    arquivo = open(localizacaoDisciplinas, "w", encoding="utf8")
    texto = json.dumps(databaseDisciplinas, indent=4)
    arquivo.write(texto)
    arquivo.close()
    
    return "Aluno e disciplina atualizados com sucesso!"


def nomeDoObjeto(localizacao, chave):
    database = carregarDados(localizacao)
    for key, value in database.items():
        if key == chave:
            return value["Nome"]


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
                        if dado == "Estoque":
                            dicionario[dado] = int(input(f"{dado}: "))
                        elif dado == "Preço de Compra" or dado == "Preço de Venda":
                            dicionario[dado] = float(input(f"{dado}: "))
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


def pesquisar(localizacao, titulo):
    disciplinasComNome = []
    tamanhoNome = len(titulo)
    database = carregarDados(localizacao)
    for codigo, disciplinas in database.items():
        for key, value in disciplinas.items():
            if key == "Nome":
                if value[0:tamanhoNome] == titulo:
                    disciplinasComNome.append(codigo)

    if len(disciplinasComNome) == 0:
        print("Não foi encontrado nenhum produto com este título.")
    else:
        for codigo, disciplinas in database.items():
            if codigo in disciplinasComNome:
                for key, value in disciplinas.items():
                    if key == "Nome":
                        print(f"{codigo} - {value}")


def relatorio(localizacao):
    database = carregarDados(localizacao)
    for key, value in database.items():
        print(f"Código: {key}")
        for chave, valor in value.items():
            if (chave != "Descrição") and (chave != "Estoque"):
                print(f"{chave}: {valor}")
        print("---")


def exportarFornecedores(localizacao):
    database = carregarDados(localizacao)
    infoFornecedores = []
    for codigoFornecedor, fornecedor in database.items():
        dadosFornecedor = [codigoFornecedor]
        for dados in fornecedor.values():
            dadosFornecedor.append(dados)
        infoFornecedores.append(",".join(dadosFornecedor))
        dadosFornecedor.clear()

    arquivo = open("exportarFornecedores.txt", "w", encoding="utf8")
    tamanhoLista = len(infoFornecedores) - 1
    for i, fornecedor in enumerate(infoFornecedores):
        if i == tamanhoLista:
            arquivo.write(fornecedor)
        else:
            arquivo.write(f"{fornecedor}\n")
    arquivo.close()

