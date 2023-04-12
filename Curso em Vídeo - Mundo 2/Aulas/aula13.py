import time
Uc = int(input('=> How many "Good Mornings" do you want? '))
for c in range(1, Uc+1):
    print(f'=> Good Morning #{c}')
    time.sleep(0.5)

print('------------')

value = int(input('=> How many numbers you wanna sum? '))
sum = 0
for c in range(1, value+1):
    number = int(input(f'=> What is the number #{c}? '))
    sum += number
print(f'=> The sum of the numbers equals: {sum}')