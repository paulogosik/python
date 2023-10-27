def inserir_usuario(login, nome, ultimoacesso, maquina):
    user = f"{login};{nome};{ultimoacesso};{maquina}"
    arquivo = open("usuarios.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()

    usersCriados = []
    for line in conteudo:
        valor = line.split(";")
        usersCriados.append(valor[0])
    arquivo.close()

    if login in usersCriados:
        print("Usuário já existe!")
    else:
        print("Usuário criado com sucesso!")
        arquivo = open("usuarios.txt", "a", encoding="utf8")
        user = f"{login};{nome};{ultimoacesso};{maquina}"
        arquivo.write(f"\n{user}")


def listar_nomes():
    arquivo = open("usuarios.txt", "r", encoding="utf8")
    usuarios = arquivo.readlines()
    print("Nomes dos usuários:")

    for usuario in usuarios:
        valor = usuario.split(";")
        print(valor[1])


def listar_dados(user):
    arquivo = open("usuarios.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    usersCriados = []
    for line in conteudo:
        valor = line.split(";")
        usersCriados.append(valor[0])

    if user not in usersCriados:
        return False
    else:
        for line in conteudo:
            usuario = line.split(";")
            if user == usuario[0]:
                return usuario


def ultimo_acesso(ultimoacesso):
    arquivo = open("usuarios.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()

    usuariosUltimoAcesso = []
    for line in conteudo:
        valor = line.split(";")
        if ultimoacesso == valor[2]:
            usuariosUltimoAcesso.append(valor[0])

    if len(usuariosUltimoAcesso) == 0:
        return False
    else:
        return usuariosUltimoAcesso


def alterar_dados(user):
    print("-" * 15)
    print("Informe o dado que você deseja alterar\n"
          "\t[1] Todos os dados\n"
          "\t[2] Nome\n"
          "\t[3] Último acesso\n"
          "\t[4] Máquina\n")
    opc = int(input(">> "))
    print("-" * 15)


def deletar_usuario(user):
    arquivo = open("usuarios.txt", "r+", encoding="utf8")
    conteudo = arquivo.readlines()

    userTemporario = []
    for valores in conteudo:
        valores = valores.replace("\n", "")
        usuario = valores.split(";")
        if usuario[0] != user:
            userTemporario.append(";".join(usuario))

    arquivo.truncate(0)
    arquivo.seek(0)
    tamanho = len(userTemporario) - 1
    for pos, usuario in enumerate(userTemporario):
        if pos == tamanho:
            arquivo.writelines(f"{usuario}")
        else:
            arquivo.writelines(f"{usuario}\n")
