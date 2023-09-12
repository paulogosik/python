def maiorValor(lista):
    maiorValor = 0
    for valor in lista:
        if valor > maiorValor:
            maiorValor = valor
    return maiorValor

def quantidade(lista, valor):
    quantidade = lista.count(valor)
    return quantidade

def quantidadeVarios(lista, valor1, valor2, valor3, valor4):
    print(f"Quantidade de {valor1} na lista é: {lista.count(valor1)}")
    print(f"Quantidade de {valor2} na lista é: {lista.count(valor2)}")
    print(f"Quantidade de {valor3} na lista é: {lista.count(valor3)}")
    print(f"Quantidade de {valor4} na lista é: {lista.count(valor4)}")

def imprimePrimeirosXValores(lista, valor):
    for i in range(valor):
        print(lista[i])

def somaXValores(lista, valor):
    soma = 0
    for i in range(valor):
        soma += lista[i]
    return soma

def imprimeOrdemCrescente(lista):
    lista2 = lista[:]
    lista2.sort()
    for valor in lista2:
        print(valor)
        
def imprimeOrdemDecrescente(lista):
    lista2 = lista[:]
    lista2.sort(reverse = True)
    for valor in lista2:
        print(valor)

def imprimeVizinhosDeX(lista, valor):
    final = len(lista)
    for i in range(final):
        if i == 0:
            if lista[i] == valor:
                print(lista[i + 1])
        elif i == final - 1:
            if lista[i] == valor:
                print(lista[i - 1])
        elif lista[i] == valor:
            print(lista[i - 1], lista[i + 1])