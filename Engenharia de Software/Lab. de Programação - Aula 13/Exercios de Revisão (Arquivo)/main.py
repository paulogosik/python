from funcoes import *

usuarios = dict()
usuarios['mickey'] = {"Login": "mickey", "Nome": "Mickey Mouse", "Último acesso": "22/06/2021", "Máquina": "larc01"}
usuarios['minnie'] = {"Login": "minnie", "Nome": "Minerva Mouse", "Último acesso": "21/06/2021", "Máquina": "lab15"}

while True:
      print(f"Escolha uma das opções abaixo:\n"
            "\t[1] Inserir usuário\n"
            "\t[2] Listar os nomes dos usuários\n"
            "\t[3] Listar dados de um usuário\n"
            "\t[4] Listar usuários com último acesso específico\n"
            "\t[5] Alterar dados de um usuário\n"
            "\t[6] Excluir um usuário\n"
            "\t[0] Sair")
      opc = int(input(">>> "))
      print("-" * 30)

      if opc == 1:
            login_novo_usuario, novo_usuario = inserir_usuario()
            usuarios[login_novo_usuario] = novo_usuario
            print("-" * 15)
            print(f"Usuário adicionado com sucesso!")
            print("-" * 30)

      elif opc == 2:
            listar_nomes(usuarios)
            print("-" * 30)

      elif opc == 3:
            listar_dados(usuarios)
            print("-" * 30)

      elif opc == 4:
            ultimo_acesso(usuarios)
            print("-" * 30)

      elif opc == 5:
            user = input("Informe o usuário que você deseja alterar informações: ")
            dados_alterados = alterar_dados(usuarios.get(user).copy())
            usuarios[user] = dados_alterados
            print("-" * 30)

      elif opc == 6:
            user = input("Informe o usuário que você deseja excluir: ")
            deletar_usuario(user=user, usuarios=usuarios)
            print("-" * 15)
            print("Usuário excluído com sucesso!")
            print("-" * 30)

      elif opc == 0:
            break