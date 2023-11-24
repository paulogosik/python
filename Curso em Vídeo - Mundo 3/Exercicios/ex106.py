from time import sleep

class color:
    p = '\033[95m'
    c = '\033[96m'
    dc = '\033[36m'
    bl = '\033[94m'
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'
    bo = '\033[1m'
    und = '\033[4m'
    end = '\033[0m'
    i = '\x1B[3m'
    w = '\033[37m'


def writeIt(phrase, textColor="\033[37m", lineColor="\033[37m"):
    length_phrase = len(phrase) + 4
    print(f"{color.bo}{lineColor}~{color.end}" * length_phrase)
    print(f"{color.bo}{textColor}{phrase:^{length_phrase}}{color.end}")
    print(f"{color.bo}{lineColor}~{color.end}" * length_phrase)


def searchFunction(name):
    writeIt(f"Searching the document of the function\'{name}\'", color.bl, color.bl)
    sleep(1)
    help(name)
    clearTerminal = input(f"{color.g}{color.bo}{color.i}Press Enter to continue.{color.end}")
    print(f"{color.p}{color.bo}={color.end}" * 120)


while True:
    writeIt("Help System - PyHelp", color.y, color.y)
    opc = input("Type the function or the library. >>> ").lower()

    if opc == "exit":
        break
    else:
        searchFunction(opc)
