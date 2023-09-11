def primeiras_letras(frase):
    palavras = frase.split(" ")
    listaPrimeiras = []
    for palavra in palavras:
        listaPrimeiras.append(palavra[0])
    primeirasLetras = '. '.join(listaPrimeiras)
    
    return primeirasLetras