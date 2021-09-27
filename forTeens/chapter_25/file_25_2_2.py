STUDENTS = 30
grades_table = {"A": "90-100", "B": "80-89", "C": "70-79", \
                "D": "60-69", "E": "0-59", "F": "0-59"}

names = [None] * STUDENTS
grades = [None] * STUDENTS

for i in range(STUDENTS):
    names[i] = input("Enter student name No" + str(i + 1) + ": ")
    grades[i] = input("Enter his or her grade: ")

for i in range(STUDENTS):
    grade = grades[i]
    grade_as_percentage = grades_table[grade]

    print(names[i], grade_as_percentage)
