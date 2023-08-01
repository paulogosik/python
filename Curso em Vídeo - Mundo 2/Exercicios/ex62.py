firstTerm = int(input("=> Inform randomly a first term: "))
ratio = int(input("=> Now, inform the ratio: "))
pa = firstTerm
terms = 10
i = 0

while terms != 0:
    i = 0
    while i <= terms:
        print(pa)
        pa += ratio
        i += 1
    terms = int(input("=> How much terms do you wanna see more? "))