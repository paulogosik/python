# def gravarAlunos(nomeArquivo):
#     arquivo = open(nomeArquivo, 'w')
#     alunosTexto = json.dumps(alunos, indent=4)
#     arquivo.write(alunosTexto)
#     arquivo.close()

# def leAlunos(nomeArquivo):
#     arquivo = open(nomeArquivo, 'r')
#     alunosTexto = arquivo.read()
#     alunos = json.loads(alunosTexto)
#     print(alunos['1']['nome'])
localizacaoArquivo = "C:/Users/paulomoita/Documents/python/Engenharia de Software/Lab. de Programação - Aula 14/Trabalho em Dupla/alunos.txt"

def alunoExiste(matricula):
    arquivo = open(localizacaoArquivo, "r", encoding="utf8")
    conteudo = arquivo.readlines()
    usersCriados = []
    for line in conteudo:
        valor = line.split(";")
        usersCriados.append(valor[0])
    arquivo.close()

    if matricula in usersCriados:
        return True
    
def alunoNaoExiste(matricula):
    arquivo = open(localizacaoArquivo, "r", encoding="utf8")
    conteudo = arquivo.readlines()
    usersCriados = []
    for line in conteudo:
        valor = line.split(";")
        usersCriados.append(valor[0])
    arquivo.close()

    if matricula not in usersCriados:
        return True

def inserir_aluno(matricula, nome):
    arquivo = open(localizacaoArquivo, "a", encoding="utf8")
    user = f"{matricula};{nome}"
    arquivo.write(f"\n{user}")
    return matricula


def listar_nomes():
    aluno = dict()
    arquivo = open(localizacaoArquivo, "r", encoding="utf8")
    usuarios = arquivo.readlines()
    print("Nomes dos usuários:")

    for usuario in usuarios:
        valor = usuario.split(";")
        aluno["Matrícula"] = valor[0]
        aluno["Nome"] = valor[1].replace("\n", "")
        print(f"{aluno['Matrícula']} - {aluno['Nome']}")

def informar_notas(matricula, n1, n2, n3, n4):
    nome = None
    aluno = dict()

    arquivo = open(localizacaoArquivo, "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for linha in conteudo:
        valores = linha.split(";")
        if valores[0] == matricula:
            aluno["Nome"] = valores[1].replace("\n", "")
    
    aluno["N1"] = n1
    aluno["N2"] = n2
    aluno["N3"] = n3
    aluno["N4"] = n4
    
    deletar_aluno(matricula)
    arquivo = open(localizacaoArquivo, "a", encoding="utf8")
    user = f"{matricula};{aluno['Nome']};{aluno['N1']};{aluno['N2']};{aluno['N3']};{aluno['N4']}"
    arquivo.write(f"\n{user}")

def pesquisarAluno(nome):
    tamanhoNome = len(nome)
    alunos = []
    aluno = dict()
    arquivo = open(localizacaoArquivo, "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for linha in conteudo:
        valores = linha.split(";")
        nomeAtual = valores[1].replace("\n", "")
        # print(nomeAtual[0:tamanhoNome])
        if nomeAtual[0:tamanhoNome] == nome:
            aluno["Matricula"] = valores[0]
            aluno["Nome"] = valores[1].replace("\n", "")
            aluno["N1"] = int(valores[2])
            aluno["N2"] = int(valores[3])
            aluno["N3"] = int(valores[4])
            aluno["N4"] = int(valores[5])
            aluno["Média"] = (aluno["N1"] + aluno["N2"] + aluno["N3"] + aluno["N4"]) / 4
            if aluno["Média"] >= 7:
                aluno["Situação"] = "Aprovado"
            else:
                aluno["Situação"] = "Reprovado"
            alunos.append(aluno.copy())
    
    for aluno in alunos:
        for key, value in aluno.items():
            print(f"{key}: {value}")
        print("-" * 15)


def deletar_aluno(matricula):
    arquivo = open(localizacaoArquivo, "r+", encoding="utf8")
    conteudo = arquivo.readlines()

    alunoTemporario = []
    for valores in conteudo:
        valores = valores.replace("\n", "")
        usuario = valores.split(";")
        if usuario[0] != matricula:
            alunoTemporario.append(";".join(usuario))

    arquivo.truncate(0)
    arquivo.seek(0)
    tamanho = len(alunoTemporario) - 1
    for pos, usuario in enumerate(alunoTemporario):
        if pos == tamanho:
            arquivo.writelines(f"{usuario}")
        else:
            arquivo.writelines(f"{usuario}\n")

def alunos_sem_notas():
    contador = 0

    arquivo = open(localizacaoArquivo, "r+", encoding="utf8")
    conteudo = arquivo.readlines()

    for valores in conteudo:
        valores = valores.replace("\n", "")
        aluno = valores.split(";")
        if len(aluno) < 3:
            print(f"{aluno[0]} - {aluno[1]}")
            contador += 1
        
    if contador == 0:
        return False

def relatorio_final():
    alunos = []
    aluno = dict()
    arquivo = open(localizacaoArquivo, "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for linha in conteudo:
        valores = linha.split(";")
        print(valores)
        if len(valores) > 4:
            aluno["Matricula"] = valores[0]
            aluno["Nome"] = valores[1].replace("\n", "")
            aluno["N1"] = int(valores[2])
            aluno["N2"] = int(valores[3])
            aluno["N3"] = int(valores[4])
            aluno["N4"] = int(valores[5])
            aluno["Média"] = (aluno["N1"] + aluno["N2"] + aluno["N3"] + aluno["N4"]) / 4
            if aluno["Média"] >= 7:
                aluno["Situação"] = "Aprovado"
            else:
                aluno["Situação"] = "Reprovado"
                alunos.append(aluno.copy())
    
    for aluno in alunos:
        print(f"{aluno['Matricula']} - {aluno['Nome']} | Média: {aluno['Média']} | {aluno['Situação']}")
        