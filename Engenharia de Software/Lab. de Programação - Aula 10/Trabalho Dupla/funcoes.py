char_ascii = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", "", ",", "-", '.', '/', "0", "1", "2", "3",
              "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H",
              "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]",
              "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]


def codificar_senha(senha_digitada):
    senha = []

    for pos, char in enumerate(senha_digitada):
        for p, c in enumerate(char_ascii):
            if c == char:
                senha.append(char_ascii[p + 3])

    senha.reverse()

    tamanho_senha = len(senha) - 1
    ultima_pos = senha.pop(tamanho_senha)
    primeira_pos = senha.pop(0)

    senha.append(primeira_pos)
    senha.insert(0, ultima_pos)
    senhaFinal = ''.join(senha)

    return senhaFinal


def decodificar_senha(senha_digitada):
    senha = []

    for pos, char in enumerate(senha_digitada):
        for p, c in enumerate(char_ascii):
            if c == char:
                senha.append(char_ascii[p - 3])

    senha.reverse()

    tamanho_senha = len(senha) - 1
    ultima_pos = senha.pop(tamanho_senha)
    primeira_pos = senha.pop(0)

    senha.append(primeira_pos)
    senha.insert(0, ultima_pos)
    senhaFinal = ''.join(senha)

    return senhaFinal
