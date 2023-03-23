i = 0

while i < 10:
    print("=> Escolha uma das opções de iluminação abaixo:\n"
          "     [A] Iluminação A\n"
          "     [B] Iluminação B\n"
          "     [C] Iluminação C")
    iluminacao = input("=> ")
    medida = float(input("=> Medida do cômodo em m²: "))
    iluminacao = iluminacao.upper()

    if iluminacao == "A":
        potencia = medida * 15
    elif iluminacao == "B":
        potencia = medida * 18
    elif iluminacao == "C":
        potencia = medida * 20
    else:
        print("=> Opção inválida!")
    print(f"=> Potência necessária para esse cômodo: {potencia}")
    if potencia % 60 == 0:
        lampadas = potencia / 60
        print(f"=> Número de lâmpadas necessárias: {lampadas}")
        print("----------------------------")
    elif potencia % 60 != 0:
        lampadas = (potencia // 60) + 1
        print(f"=> Número de lâmpadas necessárias: {lampadas}")
        print("----------------------------")