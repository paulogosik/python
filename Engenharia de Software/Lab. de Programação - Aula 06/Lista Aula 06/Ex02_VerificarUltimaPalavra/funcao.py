def eUltimaPalavra(frase):
    palavras = frase.split(" ")
    ultimaPalavra = palavras[-1].capitalize()
    
    palavrasSelecionadas = ("Junior", "Filho", "Neto", "Sobrinho")
    
    if ultimaPalavra in palavrasSelecionadas:
        return True
    else:
        return False