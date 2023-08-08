# EXERCICIO  01 --------------------------------------
def VerificaPositivo(valor):
    if valor > 0:
        return True
    else:
        return False

verif = VerificaPositivo(0)
print(verif)

# EXERCICIO  02 --------------------------------------
def VerificaPositivo(valor):
    if valor > 0:
        verif = "positivo"
    elif valor < 0:
        verif = "negativo"
    else:
        verif = "zero"
    return verif

verif = VerificaPositivo(-4)
print(f"O valor N é {verif}")