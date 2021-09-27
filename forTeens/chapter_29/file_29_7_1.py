import math

class DoingMath:
    def square(self, x):            #argument x accepts passed value
        print("The square of", x, "is", x * x)

    def square_root(self, x):       #argument x accepts passed value
        if x < 0:
            print("Cannot calculate square root")
        else:
            print("Square root of", x, "is", math.sqrt(x))
        
    def display_results(self, x):   #argument x accepts passed value
        self.square(x)
        self.square_root(x)

#Main code starts here
dm = DoingMath()

b = float(input("Enter a number: "))
dm.display_results(b)
