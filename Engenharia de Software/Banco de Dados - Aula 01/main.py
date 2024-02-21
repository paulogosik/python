from funcoes import *

localizacaoAlunos = "C:/Users/pgosi/OneDrive/Documentos/python/Engenharia de Software/Banco de Dados - Aula 01/alunos.json"
localizacaoDisciplinas = "C:/Users/pgosi/OneDrive/Documentos/python/Engenharia de Software/Banco de Dados - Aula 01/disciplinas.json"

while True:
        print(f"Escolha uma das opções abaixo:\n"
                "\t[1] Registrar novo aluno\n"
                "\t[2] Adicionar disciplina ao aluno\n"
                "\t[3] Excluir aluno\n"
                "\t[4] Cadastrar disciplina\n"
                "\t[5] Editar disciplina\n"
                "\t[6] Excluir disciplina\n"
                "\t[7] Pesquisar disciplina\n"
                "\t[8] Relatório de disciplinas cadastradas\n"
                "\t[9] Relatório de alunos cadastrados\n"
                "\t[0] Sair")
        opc = int(input(">>> "))
        print("-" * 30)

        if opc == 1:
            cgu = input("Informe o cgu do aluno: ")
            if verificarChave(localizacaoAlunos, cgu):
                print("Este código já esta cadastrado!")
                print("-" * 30)
            else:
                aluno = dict()
                nomeAluno = input("Informe o nome do aluno: ")
                codigoDisciplina = input("Informe o código da disciplina deste aluno: ")
                if not verificarChave(localizacaoDisciplinas, codigoDisciplina):
                    print("Esta disciplina não está cadastrada!")
                    print("-" * 30)
                else:
                    nomeDisciplina = nomeDoObjeto(localizacaoDisciplinas, codigoDisciplina)
                    aluno[cgu] = {
                        "Nome": nomeAluno,
                        "Disciplina(s)": nomeDisciplina
                    }

                    gravarDados(localizacaoAlunos, aluno)
                    print("-" * 30)

        elif opc == 2:
            cgu = input("Informe o CGU do aluno: ")
            if verificarChave(localizacaoAlunos, cgu):
                codigoDisciplina = input("Informe o código da disciplina: ")
                if verificarChave(localizacaoDisciplinas, codigoDisciplina):
                    retorno = atualizarDados(localizacaoAlunos, localizacaoDisciplinas, cgu, codigoDisciplina)
                    print(retorno)
                    print("-" * 30)
                else:
                    print("Esta disciplina não existe no sistema!")
                    print("-" * 30)
            else:
                print("Este aluno não existe no sistema!")
                print("-" * 30)
            

        elif opc == 3:
            cgu = input("Informe o cgu do aluno: ")
            if verificarChave(localizacaoAlunos, cgu):
                excluirItem(localizacaoAlunos, cgu)
                print("-" * 30)
            else:
                print("Este código não existe no sistema!")
                print("-" * 30)

        elif opc == 4:
            codigoDisciplina = input("Informe o código da disciplina: ")
            if verificarChave(localizacaoDisciplinas, codigoDisciplina):
                print("Esta disciplina já esta cadastrada!")
                print("-" * 30)
            else:
                disciplina = dict()
                nomeDisciplina = input("Informe o nome da disciplina: ")
                nomeProfessor = input("Informe o nome do professor desta disciplina: ")

                disciplina[codigoDisciplina] = {
                    "Nome": nomeDisciplina,
                    "Professor": nomeProfessor
                }
                gravarDados(localizacaoDisciplinas, disciplina)
                print("-" * 30)

        elif opc == 5:
            codigoDisciplina = input("Informe o código da disciplina: ")
            if verificarChave(localizacaoDisciplinas, codigoDisciplina):
                alterarDados(localizacaoDisciplinas, codigoDisciplina)
                print("Dado(s) atualizado(s)!")
                print("-" * 30)
            else:
                print("Esta disciplina não existe no sistema!")
                print("-" * 30)

        elif opc == 6:
            codigoDisciplina = input("Informe o código da disciplina: ")
            if verificarChave(localizacaoDisciplinas, codigoDisciplina):
                excluirItem(localizacaoDisciplinas, codigoDisciplina)
                print("-" * 30)
            else:
                print("Este produto não existe no sistema!")
                print("-" * 30)

        elif opc == 7:
            produto = input("Informe a disciplina que você deseja pesquisar: ")
            pesquisar(localizacaoDisciplinas, produto)
            print("-" * 30)

        elif opc == 8:
            relatorio(localizacaoDisciplinas)

        elif opc == 9:
            relatorio(localizacaoAlunos)

        elif opc == 0:
            break
