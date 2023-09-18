peopleData = []
data = []
lowestWeights = []
highestWeights = []
highestWeight = lowestWeight = 0

option = None
while option != "N":
    data.append(input("=> Type the name of the person: "))
    data.append(float(input("=> Inform the weight of the person: ")))
    option = input("=> DO you want to continue? [Y/N] ").upper()
    print("-----------------")

    peopleData.append(data[:])
    data.clear()

for i in range(len(peopleData)):
    actualWeight = peopleData[i][1]
    if i == 0:
        highestWeight = actualWeight
        lowestWeight = actualWeight
    elif actualWeight > highestWeight:
        highestWeight = actualWeight
    elif actualWeight < lowestWeight:
        lowestWeight = actualWeight

for personData in peopleData:
    if personData[1] == highestWeight:
        highestWeights.append(personData[0])
    elif personData[1] == lowestWeight:
        lowestWeights.append(personData[0])

print(f"Highest weight: {highestWeight:.1f}kg | Weight of: {highestWeights}")
print(f"Lowest weight: {lowestWeight:.1f}kg | Weight of: {lowestWeights}")
