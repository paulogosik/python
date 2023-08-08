def VerificaPositivo2(valor):
    if valor > 0:
        verif = "positivo"
    elif valor < 0:
        verif = "negativo"
    else:
        verif = "zero"
    return verif