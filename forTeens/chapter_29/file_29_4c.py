class Titan:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

#Main code starts here
titan1 = Titan("Cronus", "male")
titan2 = Titan("Oceanus", "male")
titan3 = Titan("Rhea", "female")
titan4 = Titan("Phoebe", "female")

print(titan1.name, "-", titan1.gender)
print(titan2.name, "-", titan2.gender)
print(titan3.name, "-", titan3.gender)
print(titan4.name, "-", titan4.gender)
