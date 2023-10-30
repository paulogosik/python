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
        return False
    else:
        arquivo = open("usuarios.txt", "r", encoding="utf8")
        arquivo.seek(0)
        arquivo = open("usuarios.txt", "a", encoding="utf8")
        user = f"{login};{nome};{ultimoacesso};{maquina}"
        arquivo.write(f"\n{user}")
        return login


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


def alterar_dados(user, opc):
    login_user = nome_user = acesso_user = maquina_user = None

    arquivo = open("usuarios.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    usersCriados = []
    for line in conteudo:
        valor = line.split(";")
        usersCriados.append(valor[0])
    arquivo.close()
    if user not in usersCriados:
        return False

    arquivo = open("usuarios.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for line in conteudo:
        usuario = line.split(";")
        if usuario[0] == user:
            login_user = usuario[0]
            nome_user = usuario[1]
            acesso_user = usuario[2]
            maquina_user = usuario[3]

    print("-" * 15)
    if opc == 1:
        login_user = input("Informe o login: ")
        nome_user = input("Informe o nome: ")
        acesso_user = input("Informe o último acesso: ")
        maquina_user = input("Informe a máquina: ")
    elif opc == 2:
        nome_user = input("Informe o nome: ")
    elif opc == 3:
        acesso_user = input("Informe o último acesso: ")
    elif opc == 4:
        maquina_user = input("Informe a máquina: ")

    deletar_usuario(user)
    inserir_usuario(login_user, nome_user, acesso_user, maquina_user)


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
