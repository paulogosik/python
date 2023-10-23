usuarios = dict()
usuarios['mickey'] = {"Login": "mickey", "Nome": "Mickey Mouse", "Último acesso": "22/06/2021", "Máquina": "larc01"}
usuarios['minnie'] = {"Login": "minnie", "Nome": "Minerva Mouse", "Último acesso": "21/06/2021", "Máquina": "lab15"}

while True:
    print(f"Escolha uma das opções abaixo:\n"
          "\t[1] Inserir usuário\n"
          "\t[2] Listar os nomes dos usuários\n"
          "\t[3] Listar dados de um usuário\n"
          "\t[4] Listar usuários com último acesso específico\n"
          "\t[5] \n"
          "\t[6] Inserir usuário\n"
          "\t[999] Sair")
