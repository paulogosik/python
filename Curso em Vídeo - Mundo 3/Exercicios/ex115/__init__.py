import os
import json


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


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def LoadData():
    arquivo = open('ex115.json', "r+", encoding="utf8")
    texto = arquivo.read()
    if len(texto) == 0:
        return dict()
    dicionario = json.loads(texto)
    arquivo.close()
    return dicionario


def WriteData(dictionary):
    database = LoadData()
    for key, value in dictionary.items():
       database[key] = value

    arquivo = open('ex115.json', "w", encoding="utf8")
    texto = json.dumps(database, indent=4)
    arquivo.write(texto)
    arquivo.close()


def inputAge(msg=''):
    while True:
        try:
            age = int(input(msg))
        except (ValueError, TypeError):
            print(f'{color.r}Error! Type a valid integer number.{color.end}')
        except KeyboardInterrupt:
            print(f'{color.r}Error! The user interrupted the program.{color.end}')
        else:
            return age
