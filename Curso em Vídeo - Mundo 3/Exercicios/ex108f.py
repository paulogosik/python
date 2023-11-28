def half(n):
    return n / 2


def double(n):
    return n * 2


def increase(n, percentage):
    partN = n * (percentage / 100)
    return n + partN


def decrease(n, percentage):
    partN = n * (percentage / 100)
    return n - partN


def money(num):
    num = f"{num:.2f}"
    numStr = str(num)
    formated = numStr.replace('.', ',')
    return f"R${formated}"
