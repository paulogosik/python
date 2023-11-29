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


def summary(n, increasePerc, decreasePerc):
    analysedPrice = f"R${n:.2f}".replace(".", ",")
    halfPrice = half(n)
    doublePrice = double(n)
    priceIncrease = increase(n, increasePerc)
    textIncrease = f"{increasePerc}% of increase:"
    priceDecrease = decrease(n, decreasePerc)
    textDecrease = f"{decreasePerc}% of increase:"

    print("-" * 40)
    print(f"{'SUMMARY OF THE VALUE':^40}")
    print("-" * 40)

    print(f"{'Price analyzed:':<30}", end='')
    print(f"{analysedPrice:<10}")

    print(f"{'Half the price:':<30}", end='')
    print(f"{halfPrice:<10}")

    print(f"{'Double of the price:':<30}", end='')
    print(f"{doublePrice:<10}")

    print(f"{textIncrease:<30}", end='')
    print(f"{priceIncrease:<10}")

    print(f"{textDecrease:<30}", end='')
    print(f"{priceDecrease:<10}")

    print("-" * 40)
