def half(n, f=True):
    if f:
        return money(n/2)
    else:
        return n / 2


def double(n, f=True):
    if f:
        return money(n*2)
    else:
        return n * 2


def increase(n, percentage, f=True):
    partN = n * (percentage / 100)

    if f:
        return money(n+partN)
    else:
        return n + partN


def decrease(n, percentage, f=True):
    partN = n * (percentage / 100)
    if f:
        return money(n - partN)
    else:
        return n - partN


def money(num):
    num = f"{num:.2f}"
    numStr = str(num)
    formated = numStr.replace('.', ',')
    return f"R${formated}"
