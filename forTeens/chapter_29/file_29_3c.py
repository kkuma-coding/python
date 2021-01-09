class MyClass:
    b = None   #This is a field

    def myMethod(self):
        b = "***"    #This is a local variable
        print(b, self.b, b)

#Main code starts here
x = MyClass()

x.b = "Hello!"
x.myMethod()     #It displays: *** Hello! ***
