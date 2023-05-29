import random
numeros = []
i = 0
opc = 0

while i < 10:
    numeros.append(random.randint(1,500))
    i += 1

while opc != 6:
    print(f"=> Escolha uma opção:\n"
      f"    [1] Imprime tudo\n"
      f"    [2] Imprime posição\n"
      f"    [3] Soma\n"
      f"    [4] Altera\n"
      f"    [5] Exclui\n"
      f"    [6] Encerrar")
    opc = int(input("=> "))
    
    print("--------------------------")
    if opc == 1:
        print(numeros)
    print("--------------------------")