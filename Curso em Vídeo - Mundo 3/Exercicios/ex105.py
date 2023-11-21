def grades(*nums, sit=False):
    sumGrades = higherGrade = lowerGrade = 0
    quantGrades = len(nums)

    for pos, num in enumerate(nums):
        if pos == 0:
            higherGrade = num
            lowerGrade = num
        elif num > higherGrade:
            higherGrade = num
        elif num < lowerGrade:
            lowerGrade = num

        sumGrades += num
    averageGrade = sumGrades / quantGrades

    dictionary = {
        "Total": quantGrades,
        "Higher": higherGrade,
        "Lower": lowerGrade,
        "Average": averageGrade
    }

    if sit:
        if averageGrade >= 7:
            dictionary["Situation"] = "Good"
        elif 5 < averageGrade < 7:
            dictionary["Situation"] = "Fair"
        elif averageGrade <= 5:
            dictionary["Situation"] = "Bad"
    return dictionary


student = grades(6.5, 3, 5, 5.5, sit=True)
print(student)
