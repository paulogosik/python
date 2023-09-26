from random import randint
players = dict()
playersValues = []
actualPlayer = []

print("--> Drawn values")
for i in range(1, 5):
    players[f"player{i}"] = randint(1, 6)

for key, value in players.items():
    print(f"\t{key} -> {value}")
    playersValues.append(value)

playersValues.sort(reverse=True)

print("--> Ranking")
for value in playersValues:
    for k, v in players.items():
        if v == value and k not in actualPlayer:
            print(f"\t{k} -> {v}")
            actualPlayer.append(k)
