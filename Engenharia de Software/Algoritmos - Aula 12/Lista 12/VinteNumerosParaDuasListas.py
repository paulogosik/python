lista = []
listaA = []
listaB = []

while len(lista) < 20:
    num = int(input(f"=> Informe um número inteiro {len(lista) + 1}: "))
    
    if len(lista) % 2 == 0:
        listaA.append(num)
    elif len(lista) % 2 != 0:
        listaB.append(num)
    
    lista.append(num)
    
print(f"---------------------------")
print(f"=> Lista de números com posição par: {listaA}")
print(f"=> Lista de números com posoção ímpar: {listaB}")