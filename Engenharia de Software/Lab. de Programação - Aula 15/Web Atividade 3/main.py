from funcoes import *
import json

alunos = dict()

while True:
    print(f"Escolha uma das opções abaixo:\n"
          "\t[1] Cadastrar aluno\n"
          "\t[2] Imprimir alunos\n"
          "\t[3] Informar notas\n"
          "\t[4] Pesquisar aluno\n"
          "\t[5] Excluir aluno\n"
          "\t[6] Relatório Final\n"
          "\t[0] Sair")
    opc = int(input(">>> "))
    print("-" * 30)

    # CADASTRAR ALUNO =============================
    if opc == 1:
        matricula = input("Informe a matrícula do aluno: ")
        if alunoNaoExiste(matricula):
            nome = input("Informe o nome do aluno: ")
            print("-" * 15)
            matricula = inserir_aluno(matricula, nome)
            print("Aluno criado com sucesso!")
        else:
            print("Aluno já existe!")
        print("-" * 30)

    # IMPRIMIR ALUNO =============================
    elif opc == 2:
        listar_nomes()
        print("-" * 30)

    # INFORMAR NOTAS =============================
    elif opc == 3:
        matricula = input("Qual aluno você deseja informar as notas? ")
        print("-" * 15)
        if alunoNaoExiste(matricula):
            print("Aluno não existe")
        else:
            n1 = int(input("Informa a N1 do aluno: "))
            n2 = int(input("Informa a N2 do aluno: "))
            n3 = int(input("Informa a N3 do aluno: "))
            n4 = int(input("Informa a N4 do aluno: "))
            informar_notas(matricula, n1, n2, n3, n4)
        print("-" * 30)


    # PESQUISAR ALUNO =============================
    elif opc == 4:
        nome = input("Informe o nome do aluno: ")
        print("-" * 15)
        pesquisarAluno(nome)

    # EXCLUIR ALUNO =============================
    elif opc == 5:
        matricula = input("Informe o aluno que você deseja excluir: ")

        print("-" * 15)
        if alunoExiste:
            deletar_aluno(matricula)
            print("Aluno excluído!")
        else:
            print("Aluno não encontrado!")
        print("-" * 30)

    # RELATÓRIO FINAL =============================
    elif opc == 6:
        relatorio_final()
        print("-" * 30)

    elif opc == 0:
        break
