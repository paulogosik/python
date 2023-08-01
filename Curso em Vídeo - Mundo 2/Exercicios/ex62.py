firstTerm = int(input("=> Inform randomly a first term: "))
ratio = int(input("=> Now, inform the ratio: "))
terms = int(input("=> How much terms do you wanna see? "))
pa = firstTerm
i = 0

while i <= terms:
    if i == 0:
        print(firstTerm)
    else:
        print(pa)
    pa += ratio
    i += 1