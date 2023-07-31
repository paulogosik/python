sumAges = 0
ageOlderMan = 0
nameOlderMan = ''
youngWomen = 0

for c in range(0, 4):
    name = input(f"=> Tell your name: ")
    age = int(input(f"=> Tell your age: "))
    sex = input(f"=> Inform your sex (M/F): ").upper()
    print(f"--------------")
    
    sumAges += age
    
    if sex == "M" and age > ageOlderMan:
        nameOlderMan = name
    elif sex == "F" and age < 20:
        youngWomen += 1

averageAge = sumAges / 4
print(f"=> The average of the ages is: {averageAge}")
print(f"=> The name of the older man is: {nameOlderMan}")
print(f"=> {youngWomen} women has less than 20y")