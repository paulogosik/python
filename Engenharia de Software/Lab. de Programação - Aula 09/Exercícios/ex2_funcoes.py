def naPosicao(palavra, pos):
    if pos > len(palavra):
        return -1
    else:
        return palavra[pos]
