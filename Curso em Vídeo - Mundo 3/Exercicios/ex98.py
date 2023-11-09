from time import sleep

def counter(start_num, end_num, step_num):
    if step_num == 0:
        step_num = 1
    elif step_num < 0:
        step_num *= -1

    if start_num < end_num:
        for i in range(start_num, end_num + 1, step_num):
            print(i, end=' ')
            sleep(0.3)

    elif start_num > end_num:
        for i in range(start_num, end_num - 1, step_num * -1):
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
