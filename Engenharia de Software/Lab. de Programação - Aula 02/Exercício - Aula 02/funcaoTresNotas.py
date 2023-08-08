def CalcularMedia(n1, n2, n3, tipo):
    if tipo == "A":
        media = (n1 + n2 + n3) / 3
    elif tipo == "P":
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    else:
        media = 'Vazio'
    
    return media