def maior_valor(listas):
    maiorValorGeral = 0
    
    for lista in range(len(listas)):
        maiorValorLista = 0
        for valor in range(len(listas)):
            if listas[lista][valor] > maiorValorLista:
                maiorValorLista = listas[lista][valor]
                if maiorValorLista > maiorValorGeral:
                    maiorValorGeral = maiorValorLista
        print(f"=> Maior valor da lista {lista + 1} é: {maiorValorLista}")
    print(f"=> Maior valor de todas as listas é: {maiorValorGeral}")
            
    
listas = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
maior_valor(listas)