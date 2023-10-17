def is_palindrome(palavra):
    palavraInvertida = palavra[::-1]

    if palavraInvertida == palavra:
        return True
    else:
        return False
