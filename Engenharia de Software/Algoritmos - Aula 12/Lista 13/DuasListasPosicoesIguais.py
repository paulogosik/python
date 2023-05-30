import random as r
lista1 = []
lista2 = []
posicoes = []
i = 0

n = int(input(f"=> Informe um valor N como o tamanho das listas: "))

while i < n:
    numero1 = r.randint(1, 20)
    numero2 = r.randint(1, 20)
    
    lista1.append(numero1)
    lista2.append(numero2)
    
    if numero1 == numero2:
        posicoes.append(i)
        
    i += 1

print(lista1)
print(lista2)
print(f"=> Posições que há números iguais: {posicoes}")