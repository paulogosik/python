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
            login = input("Informe o login: ").lower()
            nome = input("Informe o nome: ")
            ultimoacesso = input("Informe o último acesso: ")
            maquina = input("Informe a máquina: ")
            print("-" * 15)
            user = inserir_usuario(login, nome, ultimoacesso, maquina)
            if user:
                  print(f"Usuário {user} criado com sucesso!")
            else:
                  print("Usuário já existe")
            print("-" * 30)

      elif opc == 2:
            listar_nomes()
            print("-" * 30)

      elif opc == 3:
            login = input("Qual usuário você deseja verificar? ")
            print("-" * 15)
            usuario = listar_dados(login)
            if usuario:
                  usuario[3] = usuario[3].replace('\n', '')
                  print(f"Login: {usuario[0]}\n"
                        f"Nome: {usuario[1]}\n"
                        f"Último acesso: {usuario[2]}\n"
                        f"Máquina: {usuario[3]}")
            else:
                  print("Usuário não encontrado!")
            print("-" * 30)

      elif opc == 4:
            ultimoacesso = input("Informe o último acesso desejado: ")
            usuariosUltimoAcesso = ultimo_acesso(ultimoacesso)
            print("-" * 15)

            if usuariosUltimoAcesso:
                  print(f"Usuários com último acesso dia {ultimoacesso}:")
                  for usuario in usuariosUltimoAcesso:
                        print(usuario)
            else:
                  print("Nenhum usuário nesta data!")

            print("-" * 30)

      elif opc == 5:
            user = input("Informe o usuário que você deseja alterar informações: ")
            print("-" * 15)
            print("Informe o dado que você deseja alterar\n"
                  "\t[1] Todos os dados\n"
                  "\t[2] Nome\n"
                  "\t[3] Último acesso\n"
                  "\t[4] Máquina")
            opc = int(input(">> "))
            alterar_dados(user, opc)
            print("-" * 30)

      elif opc == 6:
            user = input("Informe o usuário que você deseja excluir: ")
            deletar_usuario(user)
            print("-" * 15)
            print("Usuário excluído com sucesso!")
            print("-" * 30)

      elif opc == 0:
            break
