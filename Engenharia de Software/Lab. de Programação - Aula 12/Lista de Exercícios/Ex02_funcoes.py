def contaTexto(frase):
    palavras = frase.split(" ")
    contaPalavras = dict()
    palavrasVerificadas = []

    for palavra in palavras:
        if palavra not in palavrasVerificadas:
            palavrasVerificadas.append(palavra)
            contaPalavras[palavra] = palavras.count(palavra)

    return contaPalavras
