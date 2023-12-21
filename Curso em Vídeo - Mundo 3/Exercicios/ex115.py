from ex115 import *
from time import sleep

while True:
    print(f"-" * 60)
    print("{:^60}".format("WELCOME TO OUR SYSTEM"))
    print("-" * 60)
    print(f'{color.g}1.{color.end} Register a new person\n'
          f'{color.g}2.{color.end} List the registered people\n'
          f'{color.r}3.{color.end} Exit the program')
    print('-' * 60)
    option = input(f'{color.g}>>> {color.end}')

    if option == '1':
        print('-' * 60)
        name = input('Enter the name of the person: ')
        age = inputAge('Enter the age of the person: ')
        person = dict()
        person[name] = age
        WriteData(person)
        print(f"\'{name}\' was successfully registered.\n")
        qstop = input('Enter any key to continue.')

    elif option == '2':
        database = LoadData()
        print('-' * 60)
        for name, age in database.items():
            print(f"{color.bo}{name} - {age} anos{color.end}")
        qstop = input('\nEnter any key to continue.')

    elif option == '3':
        break

    else:
        print(f'{color.r}Please, enter a valid option.{color.end}')
        sleep(0.8)
