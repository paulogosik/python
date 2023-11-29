def inputMoney(message=""):
    value = input(f"{message}").replace(",", ".").strip()
    while value.isalpha() or value == '':
        print(f"\033[31mError! \"{value}\" is not a valid price.\033[m")
        value = input(f"{message}").replace(",", ".").strip()

    return float(value)
