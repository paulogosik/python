num = int(input("=> Inform an integer number: "))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        cont += 1

print("---------------")
if cont == 2:
    print(f"=> {num} is a prime number!")
else:
    print(f"=> {num} is not a prime number!")