def IdadeEmDias(ano, meses, dias):
    idadeDias = (ano * 360) + (meses * 30) + dias
    return idadeDias

anos = int(input(f"=> Informe quantos anos você tem: "))
meses = int(input(f"=> Tirando os anos, quantos meses: "))
dias = int(input("=> Tirando os meses, quantos dias: "))

idadeDias = IdadeEmDias(anos, meses, dias)
print(f"=> Você tem {idadeDias} dias de idade")