from random import randint
from time import sleep

def draw():
    drawn_values = []
    print("Drawing 5 values:", end=' ')
    for i in range(5):
        num = randint(1, 10)
        drawn_values.append(num)
        print(num, end=' ')
        sleep(0.2)

    print("\nDone!")
    return drawn_values


def sumEven(drawn_values):
    sleep(0.5)
    sum = 0
    for value in drawn_values:
        if value % 2 == 0:
            sum += value

    print(f"Adding the even numbers from {drawn_values}, we have {sum} as total.")


drawnvalues = draw()
sumEven(drawnvalues)
print("-" * 30)
drawnvalues = draw()
sumEven(drawnvalues)
print("-" * 30)
drawnvalues = draw()
sumEven(drawnvalues)
