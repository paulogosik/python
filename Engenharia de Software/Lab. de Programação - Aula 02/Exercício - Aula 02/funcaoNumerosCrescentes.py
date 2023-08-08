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