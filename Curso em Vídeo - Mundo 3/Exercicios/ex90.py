student = dict()
student['Name'] = input("=> Type the name of the student: ").title()
student['Average Grade'] = float(input("=> Type the average grade of the student: "))
print("-" * 30)

if student['Average Grade'] >= 7:
    student['Situation'] = "Approved"
else:
    student['Situation'] = "Disapproved"

for key, value in student.items():
    print(f"{key}: {value}")
