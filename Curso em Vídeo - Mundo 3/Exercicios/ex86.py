matrix = [[], [], []]

for i in range(3):
    for c in range(3):
        matrix[i].append(int(input(f"=> Type the a number to [{i}, {c}]: ")))

for i in range(3):
    print(f"[ {matrix[i][0]} ] [ {matrix[i][1]} ] [ {matrix[i][2]} ]")
