class FahrenheitToCelsius:
    def __init__(self, value):
        self.temperature = value    #This calls the setter

    #Use a decorator to define the getter
    @property
    def temperature(self):
        return 5.0 / 9 * (self._temperature - 32)

    #Use a decorator to define the setter
    @temperature.setter
    def temperature(self, value):
        if value >= -459.67: 
            self._temperature = value
        else:
            raise ValueError("There is no temperature below -459.67")    

#Main code starts here
x = FahrenheitToCelsius(-50)    #This calls the constructor which, in turn, 
                                #calls the setter.
print(x.temperature)            #This calls the getter .

x.temperature = -60             #This calls the setter.
print(x.temperature)            #This calls the getter.

x.temperature = -500            #This calls the setter and throws an error

print(x.temperature)            #This is never executed. The flow of execution
                                #is stopped due to the previous statement.
