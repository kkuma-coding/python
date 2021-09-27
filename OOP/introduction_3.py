class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.height = 185

p1 = Person("John", 15)

print(p1.name)
print(p1.age)

p1.age = 16

print(p1.age)