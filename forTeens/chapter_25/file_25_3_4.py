STUDENTS = 100

names = [None] * STUDENTS
heights = [None] * STUDENTS
for i in range(STUDENTS):
    names[i] = input("Enter name for student No " + str(i + 1) + ": ")
    heights[i] = float(input("Enter his or her height: "))
    
minimum = min(heights)

print("The following students have got the shortest height:")
for i in range(STUDENTS):
    if heights[i] == minimum:
        print(names[i])
