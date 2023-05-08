i = 0

while i < 30:
    nota1 = float(input("=> Informe a primeira nota: "))
    nota2 = float(input("=> Informe a segunda nota: "))

    if nota1 < 0 or nota1 > 10:
        print(f"=> ({nota1}) Nota indisponível.")
    elif nota2 < 0 or nota2 > 10:
        print(f"=> ({nota2}) Nota indisponível.")

    media = (nota1 + nota2) / 2
    if media >= 6:
        print(f"=> Média: {media}\n"
              f"=> Situação: Aprovado")
    else:
        print(f"=> Média: {media}\n"
              f"=> Situação: Reprovado")
    i += 1
    print('--------------------------')