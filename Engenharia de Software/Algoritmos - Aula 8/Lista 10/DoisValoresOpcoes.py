n1 = float(input("=> Informe um valor N1: "))
n2 = float(input("=> Informe um valor N2: "))
print("=> Escolha uma das opções abaixo.\n"
      "     [1] Somar\n"
      "     [2] Subtrair\n"
      "     [3] Multiplicar\n"
      "     [4] Dividir\n"
      "     [5] Alterar valores\n"
      "     [6] Sair")
opc = int(input("=> "))

while opc != 6:
    if opc == 5:
        n1 = float(input("=> Informe um valor N1: "))
        n2 = float(input("=> Informe um valor N2: "))
        print("=> Escolha uma das opções abaixo.\n"
              "     [1] Somar\n"
              "     [2] Subtrair\n"
              "     [3] Multiplicar\n"
              "     [4] Dividir\n"
              "     [5] Alterar valores\n"
              "     [6] Sair")
        opc = int(input("=> "))
    
    if opc == 1:
        print(f"=> O resultado da soma é: {n1 + n2}")
    elif opc == 2:
        print(f"=> O resultado da subtração é: {n1 - n2}")
    elif opc == 3:
        print(f"=> O produto dos números é: {n1 * n2}")
    elif opc == 4:
        if n2 == 0:
            print("=> Não pode ser feita divisão por zero!")
        else:
            print(f"=> A dvisão dos números é: {(n1 / n2):.1f}")
        
    print("-------------------------------")
    n1 = float(input("=> Informe um valor N1: "))
    n2 = float(input("=> Informe um valor N2: "))
    print("=> Escolha uma das opções abaixo.\n"
          "     [1] Somar\n"
          "     [2] Subtrair\n"
          "     [3] Multiplicar\n"
          "     [4] Dividir\n"
          "     [5] Alterar valores\n"
          "     [6] Sair")
    opc = int(input("=> "))
    