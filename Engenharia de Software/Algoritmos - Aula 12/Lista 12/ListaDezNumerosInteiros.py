lista = []
listaM = []
i = 0

while i < 10:
    num = int(input(f"=> Informe um número {i + 1}: "))
    lista.append(num)
    
    if i <= 4:
        listaM.append(num*2)
    elif i > 4:
        listaM.append(num/2)
        
    i += 1
    
print(f"=> Lista: {lista}")
print(f"=> Lista depois da modificação: {listaM}")