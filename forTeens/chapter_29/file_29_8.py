class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("A school member was initialized")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != "":
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative or zero")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("A teacher was initialized")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary cannot be negative")

class Student(SchoolMember):
    def __init__(self, name, age, grades):
        SchoolMember.__init__(self, name, age)
        self.grades = grades
        print("A student was initialized")

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, values):
        #values is a list.
        #Check if negative grade exists in values
        negative_found = False
        for value in values:
            if value < 0:
                negative_found = True
                
        if negative_found == False:
            self._grades = values
        else:
            raise ValueError("Grades cannot be negative")        

#Main code starts here
teacher1 = Teacher("Mr. John Scott", 43, 35000)
teacher2 = Teacher("Mrs. Ann Carter", 5, 32000)

student1 = Student("Peter Nelson", 14, [90, 95, 92])
student2 = Student("Helen Morgan", 13, [92, 97, 94])

print(teacher1.name)
print(teacher1.age)
print(teacher1.salary)

print(student1.name)
print(student1.age)
print(student1.grades)
