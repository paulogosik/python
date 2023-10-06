from funcoes import *

while True:
    opcoes = (0, 1, 2)
    print("Escolha uma das opções:\n"
          "\t[1] Codificar senha\n"
          "\t[2] Decodificar senha\n"
          "\t[0] Sair")
    opc = int(input(">>> "))
    print("-" * 30)

    if opc not in opcoes:
        print("A opção escolhida não é válida! Tente novamente!")
        print("-" * 30)

    elif opc == 0:
        break

    elif opc == 1:
        senha_digitada = input("Digite a senha para ser codificada: ")
        print(f"SENHA CODIFICADA: {codificar_senha(senha_digitada)}")
        print("-" * 30)

    elif opc == 2:
        senha_digitada = input("Digite a senha para ser codificada: ")
        print(f"SENHA CODIFICADA: {decodificar_senha(senha_digitada)}")
        print("-" * 30)
