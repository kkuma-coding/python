class Person:
    name = None
    age = None

    def say_info(self):
        print("I am", self.name) 
        print("I am", self.age, "years old")

#Main code starts here
person1 = Person()
person1.name = "John"
person1.age = 14

person1.say_info()   #Call the method say_info() of the object person1
