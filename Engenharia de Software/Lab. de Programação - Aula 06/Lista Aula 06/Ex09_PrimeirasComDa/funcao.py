def primeiras_letras_com_da(frase):
    palavras_dadedo = ["da", "de", "das", "do", "dos", "e"]
    listaPrimeirasLetras = []
    palavras = frase.split(" ")
    
    for palavra in palavras:
        if palavra not in palavras_dadedo:
            listaPrimeirasLetras.append(palavra[0].upper())
        else:
            listaPrimeirasLetras.append(palavra.capitalize())
    
    primeirasLetras = '. '.join(listaPrimeirasLetras)
    return primeirasLetras