allStudents = []
actualStudent = []
option = None
i = 1

while option != "N":
    nameStudent = input(f"=> What's the name of the {i}º student? ").title()
    actualStudent.append(nameStudent)
    for c in range(1, 3):
        grade = float(input(f"\tStudent: {nameStudent} - {c}º Grade: "))
        actualStudent.append(grade)
    allStudents.append(actualStudent[:])

    option = input("=> Do you want to continue? [Y/N] ").upper()
    actualStudent.clear()
    i += 1
    print("-" * 45)

for student in allStudents:
    grade1 = student.pop(1)
    grade2 = student.pop(1)
    student.append((grade1 + grade2) / 2)

print(f"{'CODE':<10}", end="")
print(f"{'NAME':<25}", end="")
print(f"{'AVERAGE':>10}")
print("-" * 45)
for pos, student in enumerate(allStudents):
    print(f"{pos:0>4}      ", end="")
    print(f"{student[0]:<25}", end="")
    print(f"{student[1]:>10}")
print("-" * 45)

while True:
    studentCode = int(input(f"=> Which student do you want to show? (999 break the program) "))
    if studentCode == 999:
        break
    print(f"\tStudent: {allStudents[studentCode][0]} - Average: {allStudents[studentCode][1]}")
    print("-" * 45)
