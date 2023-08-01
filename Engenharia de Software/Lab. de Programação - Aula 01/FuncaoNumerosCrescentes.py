def OrdemCrescente(n1, n2, n3):
    if n1 > n2 and n2 > n3:
        n1 = str(n1)
        n2 = str(n2)
        n3 = str(n3)
        ordem = f"{n3}, {n2}, {n1}"
    elif n1 < n2 and n2 < n3:
        n1 = str(n1)
        n2 = str(n2)
        n3 = str(n3)
        ordem = f"{n1}, {n2}, {n3}"
    elif n1 > n2 and n2 < n3:
        n1 = str(n1)
        n2 = str(n2)
        n3 = str(n3)
        ordem = f"{n2}, {n1}, {n3}"
    elif n1 < n2 and n2 > n3:
        n1 = str(n1)
        n2 = str(n2)
        n3 = str(n3)
        ordem = f"{n1}, {n3}, {n2}"
    elif n1 < n2 and n2 > n3:
        n1 = str(n1)
        n2 = str(n2)
        n3 = str(n3)
        ordem = f"{n1}, {n3}, {n2}"
        
        
    return ordem

n1 = int(input("=> Informe um número inteiro: "))
n2 = int(input("=> Informe outro número inteiro: "))
n3 = int(input("=> Informe mais um número inteiro: "))

ordem = OrdemCrescente(n1, n2, n3)

print(f"=> A ordem crescente é: {ordem}")