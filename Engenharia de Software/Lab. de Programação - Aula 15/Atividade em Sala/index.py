from modulos import *

localizacaoLivros = "livros.json"
localizacaoClientes = "clientes.json"

while True:
        print(f"Escolha uma das opções abaixo:\n"
                "\t[1] Registrar novo livro\n"
                "\t[2] Listar livros\n"
                "\t[3] Alterar livros\n"
                "\t[4] Excluir livros\n"
                "\t[5] Pesquisar livros\n"
                "\t[6] Realizar venda\n"
                "\t[7] Relatório de vendas\n"
                "\t[0] Sair")
        opc = int(input(">>> "))
        print("-" * 30)

        if opc == 1:
            isbn = input("Informe o ISBN do livro: ")
            if verificarChave(localizacaoLivros, isbn):
                print("ISBN deste livro já está sendo usado!")
                print("-" * 30)
            else:
                livro = dict()
                tituloLivro = input("Informe o título do livro: ")
                autorLivro = input("Informe o autor do livro: ")
                generoLivro = input("Informe o gênero do livro: ")
                precocompraLivro = input("Informe o preço de compra do livro: ")
                precovendaLivro = input("Informe o preço de venda do livro: ")
                quantidadeLivro = int(input("Informe a quantidade dísponivel deste livro: "))

                livro[isbn] = {
                    "Titulo": tituloLivro,
                    "Autor": autorLivro,
                    "Genero": generoLivro,
                    "Preco de Compra": precocompraLivro,
                    "Preco de Venda": precovendaLivro,
                    "Quantidade": quantidadeLivro
                }

                gravarDados(localizacaoLivros, livro)
                print("-" * 30)

        elif opc == 2:
            databaseLivros = carregarDados(localizacaoLivros)
            for key, value in databaseLivros.items():
                print(f"{key} - {value['Titulo']} - {value['Quantidade']}")
            print("-" * 30)

        elif opc == 3:
            isbn = input("Informe o ISBN do livro: ")
            if verificarChave(localizacaoLivros, isbn):
                alterarDados(localizacaoLivros, isbn)
                print("Dado(s) atualizado(s)!")
                print("-" * 30)
            else:
                print("Este ISBN não existe no sistema!")
                print("-" * 30)

        elif opc == 4:
            isbn = input("Informe o ISBN do livro: ")
            if verificarChave(localizacaoLivros, isbn):
                excluirItem(localizacaoLivros, isbn)
                print("-" * 30)
            else:
                print("Este ISBN não existe no sistema!")
                print("-" * 30)

        elif opc == 5:
            titulo = input("Informe o titulo do livro que voce deseja pesquisar: ")
            pesquisarLivro(localizacaoLivros, titulo)
            print("-" * 30)

        elif opc == 6:
            isbn = input("Informe o ISBN do livro a ser comprado: ")
            if verificarChave(localizacaoLivros, isbn):
                cliente = dict()

                cpfCliente = input("Informe o CPF do cliente (utilize pontos e traço. Ex.: 000.000.000-00): ")
                nomeCliente = input("Informe o nome do cliente: ")
                quantidadeDesejada = int(input("Informe a quantidade desejada: "))

                cliente[cpfCliente] = {
                    "Cliente": nomeCliente,
                    "Quantidade comprada": quantidadeDesejada,
                    "ISBN": isbn
                }

                if not realizarVenda(localizacaoClientes, localizacaoLivros, cliente):
                    print("-" * 15)
                    print("Quantidade requisitada maior que a quantidade disponível.")
                else:
                    print("-" * 15)
                    print("Venda realizada com sucesso!")
                print("-" * 30)
            else:
                print("Este ISBN não existe no sistema!")
                print("-" * 30)

        elif opc == 7:
            print(7)

        elif opc == 0:
            break
