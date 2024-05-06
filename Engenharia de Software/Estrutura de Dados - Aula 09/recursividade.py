# Recursividade é a repetição de algo que se repete
# Não se pode usar 'while' ou 'for'

# Neste exemplo, a recursão acontece quando chamamos a função dentro dela mesma


def fat(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fat(n - 1)

def mult(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1:
        return y
    else:
        return y + mult(x-1, y)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

