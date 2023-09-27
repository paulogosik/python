player = dict()
players = []
goalsScored = []
sumGoals = 0
option = None

while option != "N":
    player["Name"] = input("Inform the name of the player: ").title()
    games = int(input("How many games were played: "))

    i = 0
    sumGoals = 0
    while i < games:
        goal = int(input(f"\tHow many goals were scored in the {i + 1}º match: "))
        sumGoals += goal
        goalsScored.append(goal)
        i += 1
    player["Goals"] = goalsScored[:]
    goalsScored.clear()
    player["Total of goals"] = sumGoals
    players.append(player.copy())
    player.clear()
    option = input("Do you want to continue [Y/N]? ").upper()
    if option != "N":
        print("-" * 30)
    else:
        print("-" * 60)

print(f"{'CODE':<5}", end="")
print(f"{'NAME':<20}", end="")
print(f"{'GOALS':<25}", end="")
print(f"{'TOTAL':>10}")
print("-" * 60)
for pos, player in enumerate(players):
    print(f"{(pos + 1):0>3}  ", end="")
    print(f"{player['Name']:<20}", end="")
    print(f"{str(player['Goals']):<25}", end="")
    print(f"{player['Total of goals']:>10}")
print("-" * 60)

while True:
    playerCode = int(input(f"=> Which player do you want to show [999 break the program]? "))
    if playerCode == 999:
        break
    print(f"Stats for the player {players[playerCode-1]['Name']}:")
    for position, player in enumerate(players):
        if position == playerCode-1:
            for i, goals in enumerate(player["Goals"]):
                print(f"\tIn the {i + 1}° match, {goals} goals were scored")
    print("-" * 30)
print("-" * 30)
print("THANKS!")

