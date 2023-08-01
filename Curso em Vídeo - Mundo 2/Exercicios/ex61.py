firstTerm = int(input("=> Inform randomly a first term: "))
ratio = int(input("=> Now, inform the ratio: "))
pa = firstTerm
i = 0

while i <= 10:
    if i == 0:
        print(firstTerm)
    else:
        print(pa)
    pa += ratio
    i += 1