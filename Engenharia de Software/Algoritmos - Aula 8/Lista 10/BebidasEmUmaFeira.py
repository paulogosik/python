quantidadeAgua = 0
valorAgua = 0
quantidadeRefri = 0
valorRefri = 0
quantidadeSuco = 0
valorSuco = 0 
valorConta = 0

print("=> Esolha uma das opções de bebida abaixo.\n"
      "     [A] Água\n"
      "     [R] Refrigerante\n"
      "     [S] Suco")
bebida = input("=> ")
bebida = bebida.upper()


while bebida != "SAIR":
    quantidade = int(input("=> Quantidade: "))
    
    if bebida == "A":
        valor = quantidade * 2
        valorAgua += valor
        quantidadeAgua += quantidade
    elif bebida == "R":
        valor = quantidade * 3
        valorRefri += valor
        quantidadeRefri += quantidade
    elif bebida == "S":
        valor = quantidade * 4
        valorSuco += valor
        quantidadeSuco += quantidade
        
    valorConta += valor
    
    
    print("-------------------------------")
    print("=> Esolha uma das opções de bebida abaixo.\n"
          "     [A] Água\n"
          "     [R] Refrigerante\n"
          "     [S] Suco")
    bebida = input("=> ")
    bebida = bebida.upper()
    
print("-------------------------------")
print(f"=> Total (Água)\n"
      f"    Quantidade: {quantidadeAgua}\n"
      f"    Valor: R${valorAgua}")
print(f"=> Total (Refrigerante)\n"
      f"    Quantidade: {quantidadeRefri}\n"
      f"    Valor: R${valorRefri}")
print(f"=> Total (Suco)\n"
      f"    Quantidade: {quantidadeSuco}\n"
      f"    Valor: R${valorSuco}")
print(f"=> Valor total da conta: R$ {valorConta}")