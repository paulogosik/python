adult = quantMen = youngWomen = 0

while True:
    age = int(input(f"=> Inform the age: "))
    sex = input("=> Inform the sex: [M/W] ").upper()
    
    if age > 18:
        adult += 1
    if sex == 'M':
        quantMen += 1
    elif sex == 'W' and age < 20:
        youngWomen += 1
    
    option = input("=> Do you want to continue? [Y/N] ").upper()
    print(f"-----------------")
    if option == 'N':
        break

print(f"=> People the are more than 18yo: {adult}")
print(f"=> Numbers of men: {quantMen}")
print(f"=> Women that are less than 20yo: {youngWomen}")