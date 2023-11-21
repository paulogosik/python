def fatorial(n, show=False):
    fat = 1
    for i in range(n, 0, -1):
        if show:
            if i != 1:
                print(f"{i} x ", end="")
            else:
                print(f"{i} = ", end="")
        fat *= i
    return fat


print("-" * 15)
print(fatorial(5))
print("-" * 15)
print(fatorial(8, True))
print("-" * 15)
print(fatorial(12))
print("-" * 15)
print(fatorial(18, True))
