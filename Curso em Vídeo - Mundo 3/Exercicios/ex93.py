player = dict()
goalsScored = []
sumGoals = 0

player["Name"] = input("Inform the name of the player: ").title()
games = int(input("How many games were played: "))

i = 0
while i < games:
    goal = int(input(f"\tHow many goals were scored in the {i + 1}º match: "))
    sumGoals += goal
    goalsScored.append(goal)
    i += 1

player["Goals"] = goalsScored
player["Total of goals"] = sumGoals

print("-" * 30)
for key, value in player.items():
    print(f"{key}: {value}")

print("-" * 30)
print(f"The player {player['Name']} played {len(player['Goals'])}")
for position, goal in enumerate(player["Goals"]):
    print(f"\t-> In the {position + 1}º match, scored {goal} goals")
