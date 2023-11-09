from time import sleep

def counter(startNum, endNum, stepNum):
    if stepNum == 0:
        stepNum = 1
    elif stepNum < 0:
        stepNum *= -1

    if startNum < endNum:
        for i in range(startNum, endNum + 1, stepNum):
            print(i, end=' ')
            sleep(0.3)

    elif startNum > endNum:
        for i in range(startNum, endNum - 1, stepNum * -1):
            print(i, end=' ')
            sleep(0.3)


print("------------------------------")
print("Counting from 1 to 10 (1 by 1):")
counter(1, 10, 1)

sleep(0.5)
print("\n------------------------------")
print("Counting from 10 to 0 (2 by 2):")
counter(10, 0, 2)

sleep(0.5)
print("\n------------------------------")
startNum = int(input("Type the start number: "))
endNum = int(input("Type the end number: "))
stepNum = int(input("Type the step number: "))
counter(startNum, endNum, stepNum)
print("\n------------------------------")
