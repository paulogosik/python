import random
computerChoice = random.randint(1, 10)
userChoice = int(input("=> Try to guess the number that the computer choose: "))
print("------------")

while userChoice != computerChoice:
    userChoice = int(input("=> I'm sorry, try again: "))
    print("------------")

print(f"=> Perfect, now you got it! The number was {computerChoice}")