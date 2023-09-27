person = dict()
people = []
sumAges = 0

option = None
while option != "N":
    person["Name"] = input("Type the name: ").title()
    person["Sex"] = input("Type the sex [M/F]: ").upper()
    person["Age"] = int(input("Type the age: "))

    people.append(person.copy())
    person.clear()

    option = input("Do you want to continue [Y/N]? ").upper()
    print("-" * 30)

for person in people:
    sumAges += person["Age"]
averageAge = sumAges / len(people)

print(f"- The group has {len(people)} people")
print(f"- The average age is {averageAge:.1f}")
print(f"- The women typed was:")
for person in people:
    if person["Sex"] == "F":
        print(f"\t{person['Name']}")
print(f"- The list of people above the average age is:")
for person in people:
    if person["Age"] > averageAge:
        print(f"\t{person['Name']}: {person['Age']} year old")
