from datetime import *
person = dict()

person["Name"] = input("Inform your name: ").title()
yearBirth = int(input("Inform your year of birth: "))
data = date.today()
year = data.year
person["Age"] = year - yearBirth
person["CTPS"] = int(input("Inform your Brazilian Work Card [0 if you don't have it]: "))

if person["CTPS"] != 0:
    person["Hiring Year"] = int(input("Inform your hiring year: "))
    person["Salary"] = float(input("Inform your salary: R$"))
    person["Retirement"] = (person["Hiring Year"] + 35) - yearBirth

print("-" * 30)
for key, value in person.items():
    if key == "CTPS" and value == 0:
        print("\tYou don't have a CTPS")
    elif key == "Salary":
        print(f"\t{key}: R${value}")
    else:
        print(f"\t{key}: {value}")
