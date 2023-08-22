words = ("aprender", "programar", "linguagem", "python",
            "curso", "gratis", "estudar", "praticar",
            "trabalhar", "mercado", "programador", "futuro")

vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')

for word in words:
    print(f"=> In the word {word.upper()} we have: ", end="")
    wordDivided = word.strip()
    for char in wordDivided:
        if char in vowels:
            print(f"{char} ", end='')
    print("")