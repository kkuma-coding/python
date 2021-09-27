STUDENTS = 20

names = [None] * STUDENTS
grades_lesson1 = [None] * STUDENTS
grades_lesson2 = [None] * STUDENTS
grades_lesson3 = [None] * STUDENTS

for i in range(STUDENTS):
    names[i] = input("Enter student name No" + str(i + 1) + ": ")
    grades_lesson1[i] = int(input("Enter grade for lesson 1: "))
    grades_lesson2[i] = int(input("Enter grade for lesson 2: "))
    grades_lesson3[i] = int(input("Enter grade for lesson 3: "))

#Calculate the average grade for each student
#and display the names of those who are greater than 89
for i in range(STUDENTS):
    total = grades_lesson1[i] + grades_lesson2[i] + grades_lesson3[i]
    average = total / 3.0
    if average > 89:
        print(names[i])
