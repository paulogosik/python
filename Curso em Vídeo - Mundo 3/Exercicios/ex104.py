def readInt(questionTyped=""):
    n = input(f"{questionTyped}")
    while not n.isnumeric():
        print(f"\033[31mError! You did not type a number.\033[m")
        n = input(f"{questionTyped}")

    return n


num = readInt("Type any number: ")
print(f"You typed the number {num}.")
