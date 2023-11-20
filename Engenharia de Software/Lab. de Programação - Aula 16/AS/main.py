from funcoes import *

localizacaoFornecedores = "fornecedores.json"
localizacaoProdutos = "produtos.json"

while True:
        print(f"Escolha uma das opções abaixo:\n"
                "\t[1] Registrar novo fornecedor\n"
                "\t[2] Listar fornecedores\n"
                "\t[3] Excluir fornecedor\n"
                "\t[4] Cadastrar Produto\n"
                "\t[5] Editar Produto\n"
                "\t[6] Excluir produto\n"
                "\t[7] Pesquisar produto\n"
                "\t[8] Relatório de produtos cadastrados\n"
                "\t[9] Relatório de fornecedores cadastrados\n"
                "\t[10] Exportar dados de fornecedores\n"
                "\t[0] Sair")
        opc = int(input(">>> "))
        print("-" * 30)

        if opc == 1:
            codigoFornecedor = input("Informe o código do fornecedor: ")
            if verificarChave(localizacaoFornecedores, codigoFornecedor):
                print("Este código já esta cadastrado!")
                print("-" * 30)
            else:
                fornecedor = dict()
                nomeFornecedor = input("Informe o nome do fornecedor: ")

                fornecedor[codigoFornecedor] = {
                    "Fornecedor": nomeFornecedor
                }

                gravarDados(localizacaoFornecedores, fornecedor)
                print("-" * 30)

        elif opc == 2:
            databaseFornecedores = carregarDados(localizacaoFornecedores)
            for key, value in databaseFornecedores.items():
                print(f"{key} - {value['Fornecedor']}")
            print("-" * 30)

        elif opc == 3:
            codigoFornecedor = input("Informe o código do fornecedor: ")
            if verificarChave(localizacaoFornecedores, codigoFornecedor):
                excluirItem(localizacaoFornecedores, codigoFornecedor)
                print("-" * 30)
            else:
                print("Este código não existe no sistema!")
                print("-" * 30)

        elif opc == 4:
            codigoProduto = input("Informe o código do produto: ")
            if verificarChave(localizacaoProdutos, codigoProduto):
                print("Este produto já esta cadastrado!")
                print("-" * 30)
            else:
                produto = dict()
                nomeProduto = input("Informe o nome do produto: ")
                descricaoProduto = input("Informe a descrição do produto: ")
                categoriaProduto = input("Informe a categoria do produto: ")
                precoDeCompra = float(input("Informe o preço de compra do produto: "))
                quantidadeEstoque = int(input("Informe a quantidade de estoque do produto: "))
                codigoFornecedor = input("Informe o código do fornecedor: ")
                if verificarChave(localizacaoFornecedores, codigoFornecedor):
                    fornecedorNome = nomeDoFornecedor(localizacaoFornecedores, codigoFornecedor)

                    produto[codigoProduto] = {
                        "Produto": nomeProduto,
                        "Descrição": descricaoProduto,
                        "Categoria": categoriaProduto,
                        "Estoque": quantidadeEstoque,
                        "Fornecedor": fornecedorNome,
                        "Preço de Compra": precoDeCompra,
                        "Preço de Venda": precoDeCompra + (precoDeCompra * 0.5),
                    }
                    gravarDados(localizacaoProdutos, produto)
                    atualiarFornecedor(localizacaoFornecedores, codigoFornecedor, nomeProduto)
                    print("-" * 30)
                else:
                    print("Este código não existe no sistema!")
                    print("-" * 30)

        elif opc == 5:
            codigoProduto = input("Informe o código do produto: ")
            if verificarChave(localizacaoProdutos, codigoProduto):
                alterarDados(localizacaoProdutos, codigoProduto)
                print("Dado(s) atualizado(s)!")
                print("-" * 30)
            else:
                print("Este produto não existe no sistema!")
                print("-" * 30)

        elif opc == 6:
            codigoProduto = input("Informe o código do produto: ")
            if verificarChave(localizacaoProdutos, codigoProduto):
                excluirItem(localizacaoProdutos, codigoProduto)
                print("-" * 30)
            else:
                print("Este produto não existe no sistema!")
                print("-" * 30)

        elif opc == 7:
            produto = input("Informe o produto que você deseja pesquisar: ")
            pesquisar(localizacaoProdutos, produto)
            print("-" * 30)

        elif opc == 8:
            relatorio(localizacaoProdutos)

        elif opc == 9:
            relatorio(localizacaoFornecedores)

        elif opc == 10:
            exportarFornecedores(localizacaoFornecedores)
            print("Arquivo gerado com sucesso!")

        elif opc == 0:
            break
