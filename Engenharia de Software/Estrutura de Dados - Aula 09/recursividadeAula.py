# Recursividade é a repetição de algo que se repete
# Não se pode usar 'while' ou 'for'

# Neste exemplo, a recursão acontece quando chamamos a função dentro dela mesma


def fat(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fat(n - 1)


print(fat(100))
