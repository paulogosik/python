import random
numeros = []
somaNumeros = 0
opc = 0
i = 0

while i < 100:
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
    

    if opc == 1:
        print("--------------------------")
        print(numeros)
        print("--------------------------")
        
    elif opc == 2:
        print("--------------------------")
        posicaoEscolhida = int(input("=> Escolha uma posição: "))
        i = 0
        if posicaoEscolhida > (len(numeros) - 1):
            print(f"=> Posição inválida!")
        else:
            while i < len(numeros):
                if posicaoEscolhida == i:
                    print(f"=> Número da posição escolhido: {numeros[i]}")
                i += 1
        print("--------------------------")
    
    elif opc == 3:
        print("--------------------------")
        i = 0
        while i < len(numeros):
            somaNumeros += numeros[i]
            i += 1
        print(f"=> Soma dos números: {somaNumeros}")
        print("--------------------------")
        
    elif opc == 4:
        print("--------------------------")
        novaPosicao = int(input("=> Informe uma posição: "))
        novoValor = int(input("=> Agora, informe um novo valor para essa posição: ")) 
        numeros[novaPosicao] = novoValor
        print("--------------------------")
        
    elif opc == 5:
        print("--------------------------")
        posicao = int(input("=> Informe uma posição: "))
        del(numeros[posicao])
        print("--------------------------")