# QUESTÃO 1 ------------------------------------------
def inserir_usuario():
    novo_usuario = dict()

    login = input("Informe o login do novo usuário: ")
    novo_usuario["Login"] = login
    novo_usuario["Nome"] = input("Informe o nome do novo usuário: ")
    novo_usuario["Último acesso"] = input("Informe o último acesso: ")
    novo_usuario["Máquina"] = input("Informe a máquina: ")

    return login, novo_usuario


def listar_nomes(usuarios):
    for user in usuarios.values():
        for key, value in user.items():
            if key == "Nome":
                print(f"{key}: {value}")


def listar_dados(usuarios):
    user = input("Informe um usuário para listar os dados: ")
    print("-" * 15)

    usuarios_criados = usuarios.keys()
    if user not in usuarios_criados:
        print("Usuário não encontrado!")
    else:
        user_listado = usuarios.get(user)
        for key, value in user_listado.items():
            print(f"{key}: {value}")


def ultimo_acesso(usuarios):
    acesso = input("Informe o último acesso que deseja procurar: ")
    print("-" * 15)
    print(f"Usuários com o último login dia {acesso}:")
    for user in usuarios.values():
        if user['Último acesso'] == acesso:
            print(user['Login'])


def alterar_dados(user):
    print("-" * 15)
    print("Informe o dado que você deseja alterar\n"
          "\t[1] Todos os dados\n"
          "\t[2] Nome\n"
          "\t[3] Último acesso\n"
          "\t[4] Máquina\n")
    opc = int(input(">> "))
    print("-" * 15)

    for key in user.keys():
        if opc == 1:
            if key != "Login":
                user[key] = input(f"Atualize o dado ({key}): ")

        elif opc == 2:
            if key == "Nome":
                user[key] = input(f"Atualize o dado ({key}): ")

        elif opc == 3:
            if key == "Último acesso":
                user[key] = input(f"Atualize o dado ({key}): ")

        elif opc == 4:
            if key == "Máquina":
                user[key] = input(f"Atualize o dado ({key}): ")

    return user


def deletar_usuario(user, usuarios):
    del usuarios[user]


# QUESTÃO 2 ------------------------------------------
def contaTexto(frase):
    palavras = frase.split(" ")
    contaPalavras = dict()
    palavrasVerificadas = []

    for palavra in palavras:
        if palavra not in palavrasVerificadas:
            palavrasVerificadas.append(palavra)
            contaPalavras[palavra] = palavras.count(palavra)

    return contaPalavras


# QUESTÃO 2 ------------------------------------------
def traduzir_palavra(palavra, dicionario):
    palavras_ingles = dicionario.keys()

    if palavra not in palavras_ingles:
        print("Palavra não encontrada!")
    else:
        for key, value in dicionario.items():
            if key == palavra:
                print(f"{key} -> {value}")
