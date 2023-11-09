from time import sleep

def higherNum(*nums):
    print("=" * 30)
    highernumber = 0

    if len(nums) == 0:
        print("No numbers were informed!")
        print("There is no higher number.")

    else:
        print("Numbers:", end=' ')
        for num in nums:
            sleep(0.2)
            print(num, end=' ')
            if num > highernumber:
                highernumber = num

        print(f"\nThere was informed {len(nums)} numbers")
        print(f"The higher number was: {highernumber}")

    sleep(0.5)


higherNum(2, 9, 4, 5, 7, 1)
higherNum(4, 7, 0)
higherNum(1, 2)
higherNum(6)
higherNum()
