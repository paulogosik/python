def line():
    print("-" * 30)


def message(msg):
    print(f"{msg:-^30}")


def sum_ab(a, b):
    return a + b


def counter(*num):
    if len(num) == 0:
        return "Empty elements"
    else:
        return len(num)


def dobraLista(lst):
    for pos, num in enumerate(lst):
        lst[pos] *= 2


message("Hello, World!")
message("i'm Paulo, ur creator")

print(sum_ab(2, 3))
print(sum_ab(5, 6))
print(sum_ab(1, 2))

line()
print(counter())
print(counter(1, 2, 3, 4, 5))
print(counter(6, 7, 8, 9))

line()
lista = [4, 3, 2, 0, 1]
print(f"Lista: {lista}")
dobraLista(lista)
print(f"Lista dobrada: {lista}")

line()
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista 2: {lista2}")
dobraLista(lista2)
print(f"Lista 2 dobrada: {lista2}")
