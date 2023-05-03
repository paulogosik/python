opc = 1

while opc != 4:
    print(f"=> Escolha uma das opções abaixo\n"
        f"    [1]Pode votar? \n"
        f"    [2]Ver Categoria\n"
        f"    [3]Pode alistar? \n"
        f"    [4]Encerrar programa")
    opc = int(input("=> "))
    print("---------------------------")
    
    if opc == 1:
        idade = int(input("=> Informe sua idade: "))
        nacionalidade = input("=> Informe sua nacionalidade (Ex.: Brasileiro, Argentino): ")
        nacionalidade = nacionalidade.capitalize()

        print("---------------------------")
        if nacionalidade == "Brasileiro" and idade >= 16:
            print("=> Pode votar.")
        else:
            print("=> Não pode votar.")
            
        print("---------------------------")
        
    elif opc == 2:
        idade = int(input("=> Informe a sua idade: "))
        
        print("---------------------------")
        if idade <= 11:
            print("=> Categoria: Criança")
        elif idade <= 20:
            print("=> Categoria: Adolescente")
        elif idade <= 30:
            print("=> Categoria: Jovem")
        elif idade <= 59:
            print("=> Categoria: Adulto")
        elif idade >= 60:
            print("=> Categoria: Idoso")
        print("---------------------------")
        
    elif opc == 3:
        idade = int(input("=> Informe a sua idade: "))
        sexo = input("=> Informe o seu sexo (M/F): ")
        sexo = sexo.upper()
        print("---------------------------")
        if sexo == "M" and idade >= 18:
            print("=> Deve se alistar no serviço militar.")
        else:
            print("=> Não pode se alistar no serviço militar.")
        print("---------------------------")
    
    elif opc != 1 and opc != 2 and opc != 3 and opc != 4:
        print("=> Opção inválida!")
        print("---------------------------")