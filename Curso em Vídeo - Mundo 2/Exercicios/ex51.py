firstTerm = int(input("=> Inform randomly a first term: "))
ratio = int(input("=> Now, inform the ratio: "))
pa = firstTerm

for c in range(0, 10):
    if c == 0:
        print(firstTerm)
    else:
        print(pa)
    pa += ratio