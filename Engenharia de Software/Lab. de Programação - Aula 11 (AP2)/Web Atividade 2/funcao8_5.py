def rotate_word(frase, rotacao):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    palavras = frase.split(" ")
    fraseCodificada = []

    for palavra in palavras:
        novaPalavra = []

        for char in palavra:
            posicaoChar = alfabeto.find(char) + rotacao
            if posicaoChar >= len(alfabeto):
                posicaoChar = posicaoChar - len(alfabeto)
            novaPalavra.append(alfabeto[posicaoChar])

        fraseCodificada.append(''.join(novaPalavra))
        novaPalavra.clear()

    return ' '.join(fraseCodificada)
