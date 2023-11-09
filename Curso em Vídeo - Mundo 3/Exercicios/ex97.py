def writeIt(phrase):
    length_phrase = len(phrase) + 4
    print("~" * length_phrase)
    print(f"{phrase:^{length_phrase}}")
    print("~" * length_phrase)


writeIt(input("Type the phrase to print: "))
