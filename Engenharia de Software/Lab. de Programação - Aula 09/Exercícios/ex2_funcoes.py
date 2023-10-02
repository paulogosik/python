def naPosicao(palavra, pos):
    if pos >= len(palavra):
        return -1
    else:
        return palavra[pos]


def posicoes(palavra, letra):
    for pos, let in enumerate(palavra):
        if let == letra:
            print(pos)


def iniciaCom(palavra, letra):
    if palavra[0] == letra:
        return True
    else:
        return False


def maiorPalavra(lista):
    maiorletras = 0
    maiorpalavra = None
    for palavra in lista:
        atualpalavra = 0
        for letra in palavra:
            atualpalavra += 1
        if atualpalavra > maiorletras:
            maiorpalavra = palavra

    return maiorpalavra


def ehConector(palavra):
    conectores = ["da", "de", "das", "do", "dos", "e"]
    if palavra in conectores:
        return True
    else:
        return False
