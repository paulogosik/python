def readInt(questionTyped=""):
    while True:
        try:
            n = int(input(f"{questionTyped}"))
        except (ValueError, TypeError):
            print("\033[31mERROR! Please enter a valid integer number.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mThe user interrupted the program.\033[m")
            return 0
        else:
            return n


def readFloat(questionTyped=""):
    while True:
        try:
            n = float(input(f"{questionTyped}"))
        except (ValueError, TypeError):
            print("\033[31mERROR! Please enter a valid float number.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mThe user interrupted the program.\033[m")
            return 0
        else:
            return n


integerNumber = readInt("Enter an integer number: ")
floatNumber = readFloat("Enter a float number: ")
print("-" * 15)
print(f"The integer is: {integerNumber}\n"
      f"The float is: {floatNumber}")
