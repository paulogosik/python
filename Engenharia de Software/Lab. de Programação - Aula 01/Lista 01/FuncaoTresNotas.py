def CalcularMedia(n1, n2, n3, tipo):
    if tipo == "A":
        media = (n1 + n2 + n3) / 3
    elif tipo == "P":
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    else:
        media = 'Vazio'
    
    return media
    
tipo = input("=> Informe o tipo da matéria: ").upper()
n1 = float(input(f"=> Informe a N1: "))
n2 = float(input(f"=> Informe a N2: "))
n3 = float(input(f"=> Informe a N3: "))

media = CalcularMedia(n1, n2, n3, tipo)

print(f"=> A média do aluno foi: {media}")